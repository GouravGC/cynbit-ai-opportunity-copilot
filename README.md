# Cynbit AI Opportunity Blueprint Copilot

An AI-powered proof of concept that transforms business problems into structured AI/ML opportunity blueprints using publicly available company information, TF-IDF-based retrieval, and an LLM.

**Developed for:** Cynbit AI/ML Engineer Intern Technical Assessment

## Project Links

- **Live Demo:** https://cynbit-ai-opportunity-copilot.streamlit.app/
- **GitHub Repository:** https://github.com/GouravGC/cynbit-ai-opportunity-copilot
- **AI Opportunity Report:** [Read the Industry Analysis and Recommendations](AI_OPPORTUNITY_REPORT.md)
- **Technical Approach Report:** [Read the Architecture and Implementation Plan](TECHNICAL_APPROACH.md)

## 1. Project Overview

The Cynbit AI Opportunity Blueprint Copilot helps users explore how AI/ML could address business challenges and generate a structured implementation blueprint.

The prototype retrieves relevant information from a collection of public Cynbit website sources and supplies that context to an LLM to generate a report with proposed solutions, architecture, risks, evaluation metrics, and implementation phases.

## 2. Key Features

- Business problem input through a Streamlit interface
- Retrieval of relevant information from public company sources
- TF-IDF-based text retrieval using cosine similarity
- LLM-powered opportunity analysis and blueprint generation
- Source URL references and explicit assumptions
- Proposed architecture, implementation phases, risks, and evaluation metrics
- Markdown report generation and download

## 3. Technical Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| User interface | Streamlit |
| Language model | Google Gemini 2.5 Flash via OpenRouter |
| Retrieval | Scikit-learn TF-IDF and cosine similarity |
| Testing | Pytest |
| Version control | Git and GitHub |
| Deployment | Streamlit Community Cloud |

## 4. Architecture

1. The user submits a business problem.
2. Public company source records are loaded.
3. Text is split into overlapping chunks.
4. TF-IDF retrieval ranks relevant chunks against the query.
5. Retrieved context and instructions are passed to the LLM.
6. The model generates a structured opportunity blueprint.
7. The interface displays the report and provides a Markdown download.

**Note:** The current retrieval implementation is lexical TF-IDF retrieval, not embedding-based semantic search.

## 5. Public Information Sources

- [Cynbit Services](https://www.cynbit.in/services)
- [Cynbit Contact](https://www.cynbit.in/contact)
- [Cynbit Careers](https://www.cynbit.in/careers)

These sources provide public context for the prototype. They do not establish access to Cynbit's internal data or validate the business impact of proposed opportunities.

## 6. Assessment Deliverables

### Deliverable 1: AI Opportunity Report

[Open AI_OPPORTUNITY_REPORT.md](AI_OPPORTUNITY_REPORT.md)

Evaluates potential AI/ML opportunities, prioritizes candidate use cases, recommends an initial pilot, and discusses implementation considerations, risks, and evaluation metrics.

### Deliverable 2: AI/ML Proof of Concept

[Launch the Live Demo](https://cynbit-ai-opportunity-copilot.streamlit.app/)

[Explore the Source Code](https://github.com/GouravGC/cynbit-ai-opportunity-copilot)

A working prototype demonstrating retrieval-augmented report generation using public company information and a hosted LLM.

### Deliverable 3: Technical Approach Report

[Open TECHNICAL_APPROACH.md](TECHNICAL_APPROACH.md)

Documents the system architecture, model choices, retrieval pipeline, prompt engineering, testing approach, security considerations, limitations, and proposed execution plan.

## 7. Setup and Local Execution

### Prerequisites

- Python 3.11 recommended
- An OpenRouter API key

### Installation

```bash
git clone https://github.com/GouravGC/cynbit-ai-opportunity-copilot.git
cd cynbit-ai-opportunity-copilot

python -m venv .venv
```

Activate the environment.

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your API key using an environment variable:

**Windows PowerShell:**
```powershell
$env:OPENROUTER_API_KEY="your-api-key"
```

**macOS/Linux:**
```bash
export OPENROUTER_API_KEY="your-api-key"
```

Run the Streamlit application using the entry point configured for this repository. For the current UI module, that is:

```bash
streamlit run app/ui.py
```

Never commit API keys or secret files to GitHub.

## 8. Testing

Run the automated test suite:

```bash
python -m pytest -v
```

The tests cover selected source-loading and workflow behavior. They do not independently guarantee factual accuracy of live LLM responses or production readiness.

## 9. Limitations and Future Improvements

- Expand and periodically refresh the public-source collection.
- Evaluate retrieval relevance on a labeled query set.
- Add stronger validation of generated claims and citations.
- Improve error handling, logging, and API usage monitoring.
- Evaluate output quality using representative test cases.
- Consider embedding-based retrieval and persistent indexing if evaluation justifies them.
- Conduct security, privacy, and stakeholder reviews before production deployment.

## 10. Responsible AI

The prototype is intended for exploratory analysis. Generated recommendations should be reviewed by a human, and source references should be checked before business decisions are made. The system has not been demonstrated to deliver verified cost savings or other measured business outcomes.

Reference: [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

---

**Project status:** Technical assessment proof of concept. Production deployment and business impact require further validation.