import sys
import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

from app.workflows.blueprint import create_blueprint
from app.workflows.enquiry_router import classify_enquiry


st.set_page_config(
    page_title="Cynbit AI Opportunity Copilot",
    page_icon="🤖",
    layout="wide",
)

st.title("Cynbit AI Opportunity Blueprint Copilot")
st.caption(
    "Explore AI opportunities and demonstrate an AI-powered "
    "customer enquiry classification workflow."
)

blueprint_tab, routing_tab = st.tabs(
    ["Opportunity Blueprint", "Enquiry Classification & Routing"]
)


# --------------------------------------------------
# EXISTING WORKFLOW: OPPORTUNITY BLUEPRINT
# --------------------------------------------------

with blueprint_tab:
    st.subheader("Generate an AI Opportunity Blueprint")

    inquiry = st.text_area(
        "Client business inquiry",
        height=180,
        placeholder=(
            "Describe the client's problem, goals, current workflow, "
            "and constraints..."
        ),
        key="blueprint_inquiry",
    )

    if st.button("Generate Blueprint", type="primary"):
        if not inquiry.strip():
            st.warning("Please enter a client inquiry first.")
        else:
            try:
                with st.spinner("Generating blueprint..."):
                    result = create_blueprint(inquiry)

                st.session_state["blueprint"] = result

            except Exception:
                st.error(
                    "Blueprint generation failed. Check the application "
                    "logs and API configuration."
                )

    if "blueprint" in st.session_state:
        st.subheader("Generated Opportunity Blueprint")
        st.markdown(st.session_state["blueprint"])

        st.download_button(
            "Download Blueprint",
            data=st.session_state["blueprint"],
            file_name="cynbit_opportunity_blueprint.md",
            mime="text/markdown",
        )


# --------------------------------------------------
# NEW WORKFLOW: CUSTOMER ENQUIRY CLASSIFICATION
# --------------------------------------------------

with routing_tab:
    st.subheader("AI-Powered Customer Enquiry Classification")

    st.write(
        "Classify a customer enquiry, extract its intent, and recommend "
        "a destination and next action. This prototype does not contact "
        "customers, update a CRM, or execute routing actions."
    )

    sample_enquiry = (
        "We need an AI chatbot that can qualify website leads and integrate "
        "with our CRM. Please advise on the required integrations and "
        "implementation timeline."
    )

    if "routing_enquiry_input" not in st.session_state:
        st.session_state["routing_enquiry_input"] = ""

    if st.button("Load Sample Enquiry"):
        st.session_state["routing_enquiry_input"] = sample_enquiry

    enquiry = st.text_area(
        "Customer enquiry",
        height=150,
        placeholder="Enter a sample or authorized customer enquiry...",
        key="routing_enquiry_input",
    )

    if st.button("Classify Enquiry", type="primary"):
        if not enquiry.strip():
            st.warning("Please enter an enquiry first.")
        else:
            try:
                with st.spinner("Classifying enquiry..."):
                    result = classify_enquiry(enquiry)

                st.session_state["enquiry_result"] = result

            except Exception:
                st.error(
                    "Classification failed. Check the application logs "
                    "and try again."
                )

    result = st.session_state.get("enquiry_result")

    if result:
        st.subheader("Classification Result")

        st.warning(
            "Human review is required before acting on this recommendation."
        )

        col1, col2, col3 = st.columns(3)

        col1.metric("Category", result["category"])
        col2.metric("Urgency", result["urgency"].title())
        col3.metric("Confidence", result["confidence"].title())

        st.markdown(f"**Intent:** {result['intent']}")
        st.markdown(f"**Summary:** {result['summary']}")
        st.markdown(f"**Suggested route:** {result['suggested_route']}")
        st.markdown(f"**Recommended next action:** {result['next_action']}")

        st.markdown("**Missing information:**")

        if result["missing_information"]:
            for item in result["missing_information"]:
                st.write(f"- {item}")
        else:
            st.write("No missing information identified by the model.")

        st.caption(
            "Confidence is a qualitative model estimate, not a calibrated "
            "probability. Accuracy must be evaluated on labeled examples."
        )

        st.download_button(
            "Download Classification JSON",
            data=json.dumps(result, indent=2),
            file_name="cynbit_enquiry_classification.json",
            mime="application/json",
        )