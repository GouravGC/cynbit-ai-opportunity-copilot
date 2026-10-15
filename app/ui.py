
import streamlit as st

from app.workflows.blueprint import create_blueprint


st.set_page_config(
    page_title="Cynbit Opportunity Copilot",
    page_icon="🤖",
    layout="wide",
)

st.title("Cynbit Opportunity Blueprint Copilot")
st.caption(
    "Turn client business inquiries into evidence-grounded "
    "AI solution blueprints."
)

inquiry = st.text_area(
    "Client business inquiry",
    height=180,
    placeholder=(
        "Describe the client's problem, goals, "
        "current workflow, and constraints..."
    ),
)

if st.button("Generate Blueprint", type="primary"):
    if not inquiry.strip():
        st.warning("Please enter a client inquiry first.")
    else:
        try:
            with st.spinner("Generating your blueprint..."):
                result = create_blueprint(inquiry)

            st.session_state["blueprint"] = result

        except Exception as error:
            st.error(f"Generation failed: {error}")

if "blueprint" in st.session_state:
    st.subheader("Generated Opportunity Blueprint")
    st.markdown(st.session_state["blueprint"])

    st.download_button(
        "Download Blueprint",
        data=st.session_state["blueprint"],
        file_name="cynbit_opportunity_blueprint.md",
        mime="text/markdown",
    )
