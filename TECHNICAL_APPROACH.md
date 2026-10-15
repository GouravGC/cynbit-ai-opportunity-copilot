# Technical Approach Report: Cynbit AI Opportunity Blueprint Copilot

## 1. Project Overview

**Project:** Cynbit AI Opportunity Blueprint Copilot  
**Prototype:** https://cynbit-ai-opportunity-copilot.streamlit.app/  
**Source code:** https://github.com/GouravGC/cynbit-ai-opportunity-copilot

The prototype accepts a business problem, retrieves relevant information from a small collection of public Cynbit website sources, and uses a large language model (LLM) to generate a structured AI opportunity blueprint.

The output covers the business objective, relevant services and source URLs, proposed architecture, unanswered questions, risks, implementation phases, evaluation metrics, and assumptions.

The prototype demonstrates a possible AI-assisted opportunity-analysis workflow. It does not establish that its recommendations have been validated by Cynbit or that they have delivered measurable business outcomes.

## 2. System Architecture

The workflow follows this sequence:

1. **User input:** A user describes a business problem or opportunity.
2. **Source loading:** Publicly available Cynbit information is loaded from a local source collection.
3. **Chunking:** Source text is divided into overlapping text chunks.
4. **Retrieval:** TF-IDF features and cosine similarity identify relevant chunks.
5. **Prompt construction:** The retrieved context and user query are assembled into an instruction prompt.
6. **LLM generation:** The configured Gemini 2.5 Flash model is accessed through OpenRouter.
7. **Presentation:** The Streamlit interface displays the generated blueprint and offers a Markdown download.

The retrieval component is lexical rather than embedding-based semantic search. It is intentionally lightweight for a prototype.

## 3. Model and Technology Choices

### Language model

**Model:** `google/gemini-2.5-flash` through OpenRouter.

**Rationale:** A hosted model avoids requiring local GPU inference and can generate structured natural-language analysis. The model is configured through the OpenAI-compatible client interface.

**Limitations:** Output quality depends on the prompt, retrieved context, model behavior, and available API service. Generated claims and citations require verification.

### Retrieval method

**Method:** `TfidfVectorizer` with English stop-word removal and unigram/bigram features, followed by cosine-similarity ranking.

**Configuration:** Approximately 700-character chunks, 550-character stride, and up to five retrieved chunks.

**Rationale:** TF-IDF is simple, inexpensive, and transparent for a small source collection.

**Limitations:** Lexical retrieval may miss relevant passages that use different wording. The current implementation does not provide embedding-based semantic retrieval, persistent vector indexing, or a dedicated vector database.

### Application layer

- **Streamlit:** User interface and downloadable results.
- **Python:** Workflow orchestration and text processing.
- **Pydantic:** Available for structured data validation where used.
- **Pytest:** Automated tests.
- **GitHub:** Version control and source-code hosting.
- **Streamlit Community Cloud:** Hosted demo deployment.

## 4. Data Pipeline

### Input sources

The source collection includes publicly accessible Cynbit pages, including services, contact, and careers information.

- https://www.cynbit.in/services
- https://www.cynbit.in/contact
- https://www.cynbit.in/careers

These sources provide public context, not access to Cynbit's private customer records, internal systems, or verified operational metrics.

### Processing steps

1. Load the source records.
2. Split text into overlapping chunks.
3. Transform chunks into TF-IDF vectors.
4. Transform the user query using the same vectorizer.
5. Rank chunks using cosine similarity.
6. Select the top relevant chunks.
7. Supply the selected context to the generation workflow.

### Output

The LLM generates a structured Markdown report containing the proposed opportunity, supporting source URLs, architecture, open questions, risks, implementation phases, metrics, and assumptions.

For a production system, the pipeline should add source freshness checks, metadata and provenance tracking, stronger validation, and monitoring of retrieval and generation quality.

## 5. Prompt Engineering

The generation workflow is designed to:

- Use retrieved evidence when making claims about Cynbit.
- Include source URLs for relevant public information.
- Distinguish publicly described services from proposed solutions.
- Avoid inventing internal capabilities, results, or customer information.
- Explicitly identify assumptions and unanswered questions.
- Include risks, human-review requirements, implementation phases, and evaluation metrics.

The prompt structure improves consistency but does not guarantee factual correctness. Citations must be checked against the source pages, and unsupported claims should be removed or qualified.

## 6. Evaluation and Testing

The repository includes automated tests covering source availability, expected source pages, and mocked generation behavior, including expected report sections and source references.

These tests verify aspects of workflow behavior. They do not independently prove that live LLM responses are factually correct, that every citation supports its claim, or that the system is ready for production.

### Proposed evaluation plan

**Retrieval evaluation**
- Create a set of representative queries with manually identified relevant passages.
- Measure precision at five and recall where relevant passages are labeled.
- Inspect queries for which retrieval returns irrelevant or incomplete context.

**Generation evaluation**
- Review factual accuracy, source support, completeness, and clarity.
- Measure unsupported-claim frequency and citation correctness.
- Test missing information, ambiguous requests, and adversarial inputs.

**Operational evaluation**
- Record response latency, API failures, token usage, and cost per generated report.
- Test invalid input and service errors.
- Confirm that API credentials are not exposed in the UI, logs, or repository.

## 7. Security and Responsible AI

- Keep API credentials in environment variables or approved deployment secrets.
- Never commit `.env` files or secret keys.
- Avoid submitting confidential business or customer data without authorization.
- Treat user input and retrieved website content as untrusted data.
- Require human review before acting on consequential recommendations.
- Add request limits and monitoring before broader use.
- Review retention, privacy, and access-control requirements before integrating real business systems.

Reference: NIST AI Risk Management Framework — https://www.nist.gov/itl/ai-risk-management-framework

## 8. Execution Plan

### Phase 1 — Discovery
Confirm the intended user, business problem, data access, current workflow, and measurable success criteria.

### Phase 2 — Prototype refinement
Improve source coverage, validate user inputs, strengthen error handling, and make evidence and assumptions easy to inspect.

### Phase 3 — Evaluation
Build a representative test set and measure retrieval relevance, generation accuracy, citation correctness, latency, and cost.

### Phase 4 — Controlled pilot
Test with authorized data and a limited group of users. Keep recommendations advisory and retain human approval.

### Phase 5 — Production decision
Consider additional integrations, persistent retrieval indexes, access controls, monitoring, and deployment hardening only after the pilot demonstrates sufficient quality and value.

## 9. Limitations

The current prototype uses a small public-source collection, lightweight TF-IDF retrieval, and hosted LLM generation. It is not a production RAG platform, does not connect to Cynbit's internal systems, and has not been shown to produce verified business savings.

Production readiness would require a broader evaluation dataset, stronger grounding checks, security review, monitoring, and stakeholder acceptance testing.

## 10. Conclusion

The Cynbit AI Opportunity Blueprint Copilot demonstrates an end-to-end approach for converting a business question and retrieved public context into a structured AI opportunity report. It combines transparent lexical retrieval, hosted LLM generation, a Streamlit interface, and automated workflow tests.

The next step is to evaluate the prototype against representative tasks, verify its claims and citations, and refine the workflow based on stakeholder feedback before considering a production deployment.