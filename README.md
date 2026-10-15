# Cynbit AI Opportunity Blueprint Copilot

**An AI-powered prototype that transforms business inquiries into structured, evidence-grounded AI solution blueprints.**

<p align="center">
  <a href="https://cynbit-ai-opportunity-copilot.streamlit.app/">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open Live App">
  </a>
</p>

<p align="center">
  <a href="https://cynbit-ai-opportunity-copilot.streamlit.app/"><strong>🚀 Launch Live App</strong></a>
  &nbsp; | &nbsp;
  <a href="https://github.com/GouravGC/cynbit-ai-opportunity-copilot"><strong>💻 View Source Code</strong></a>
</p>

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)
![Retrieval](https://img.shields.io/badge/Retrieval-TF--IDF-orange)
![Testing](https://img.shields.io/badge/Tests-6%20Passing-brightgreen)

## Overview

Organizations need practical ways to translate operational challenges into actionable AI opportunities. This project demonstrates an AI-assisted workflow that analyzes a client inquiry, retrieves relevant information from Cynbit's publicly available website, and generates a structured solution blueprint for human review.

The application combines lightweight information retrieval, prompt engineering, and a large language model to support early-stage business analysis and AI solution design.

## Live Demo

**Try it here:** [Cynbit AI Opportunity Blueprint Copilot](https://cynbit-ai-opportunity-copilot.streamlit.app/)

Enter a business problem in natural language and generate a structured blueprint that includes requirements, proposed architecture, risks, implementation phases, and evaluation metrics. The generated blueprint can be downloaded as a Markdown report.

## Key Features

- **Business inquiry analysis:** Converts natural-language business problems into structured requirements.
- **Retrieval-augmented generation (RAG):** Retrieves relevant passages from collected public website content and supplies them as context to the language model.
- **TF-IDF-based retrieval:** Uses word and bigram features with cosine similarity to rank relevant text chunks.
- **Source-aware recommendations:** Instructs the model to include source URLs for claims about publicly advertised services.
- **Structured blueprint generation:** Produces business objectives, requirements, proposed architecture, discovery questions, risks, implementation phases, and evaluation metrics.
- **Human-in-the-loop safeguards:** Highlights assumptions, uncertainty, missing information, and situations requiring human review.
- **Interactive Streamlit interface:** Lets users submit inquiries and inspect generated reports.
- **Markdown export:** Downloads generated blueprints for further review and editing.
- **Automated tests:** Tests basic source handling and blueprint workflow behavior.

## Example Use Case

An e-commerce company receives hundreds of customer enquiries every week and wants to reduce manual support workload.

The copilot can help draft a proposed solution covering:

- Classification of order tracking, returns, payment issues, product questions, and complaints.
- Extraction of relevant order and customer details.
- Suggested routing and priority assignment.
- Human escalation for uncertain or sensitive cases.
- Data protection, evaluation metrics, and implementation phases.

This is a proposed architecture, not a claim that the system has been integrated with a live customer-support platform.

## How It Works

1. **Data ingestion:** Collects publicly accessible content from Cynbit's services, contact, and careers pages.
2. **Text chunking:** Splits collected text into overlapping character-based chunks.
3. **Retrieval:** Uses TF-IDF vectorization and cosine similarity to rank relevant passages for a client inquiry.
4. **Prompt construction:** Combines the inquiry, retrieved evidence, source URLs, and generation requirements.
5. **LLM generation:** Calls Gemini 2.5 Flash through the OpenRouter API.
6. **Presentation and export:** Displays the blueprint in Streamlit and provides a downloadable Markdown report.

## Architecture

```text
Client Business Inquiry
          |
          v
     Streamlit UI
          |
          v
   Blueprint Workflow
          |
          v
   TF-IDF Retrieval <----- Public Cynbit Website Data
          |
          v
  Evidence-Aware Prompt
          |
          v
 Gemini 2.5 Flash via OpenRouter
          |
          v
 Structured AI Opportunity Blueprint
          |
          v
    Markdown Download
```

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python 3.11 |
| Frontend | Streamlit |
| Retrieval | scikit-learn, TF-IDF, cosine similarity |
| Language model | Gemini 2.5 Flash |
| LLM API integration | OpenAI Python SDK with OpenRouter |
| Configuration | python-dotenv |
| Testing | pytest |
| Version control | Git and GitHub |
| Deployment | Streamlit Community Cloud |

## Project Structure

```text
cynbit-ai-opportunity-copilot/
├── app/
│   ├── __init__.py
│   ├── fetch_sources.py
│   ├── llm_client.py
│   ├── main.py
│   ├── retriever.py
│   ├── ui.py
│   └── workflows/
│       ├── __init__.py
│       └── blueprint.py
├── data/
│   └── public_sources/
│       ├── cynbit_sources.json
│       └── cynbit_sources.txt
├── tests/
│   └── test_blueprint.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Run Locally

### Prerequisites

- Python 3.11
- pip
- An OpenRouter API key with access to the configured model

### 1. Clone the repository

```bash
git clone https://github.com/GouravGC/cynbit-ai-opportunity-copilot.git
cd cynbit-ai-opportunity-copilot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Ensure `requirements.txt` includes all required runtime dependencies, including scikit-learn.

### 3. Configure environment variables

Create a `.env` file in the project root:

```text
OPENROUTER_API_KEY=your_openrouter_api_key
```

Never commit your API key or other secrets to GitHub.

### 4. Launch the application

```bash
python -m streamlit run app/ui.py
```

### 5. Run the tests

```bash
python -m pytest -v
```

## Evaluation and Testing

The current test suite contains six tests covering:

- Public source file availability and structure.
- Presence of required website sources.
- Basic blueprint output structure.
- Source URL presence.
- Human-review wording.

Relevant workflow tests use mocked LLM responses. Passing these tests demonstrates basic application behavior but does not independently establish model factuality, citation entailment, retrieval quality, or production-grade guardrail effectiveness.

## Current Limitations

- Retrieval uses lexical TF-IDF similarity rather than embedding-based semantic search.
- No dedicated vector database is used.
- Website extraction may retain navigation or interface text.
- Public website content does not independently verify internal company capabilities.
- Generated recommendations may contain unsupported assumptions and require human review.
- Proposed integrations, costs, timelines, and performance must be validated before implementation.
- No production integrations or measured business impact are claimed.

## Public Information Sources

- [Cynbit Services](https://www.cynbit.in/services)
- [Cynbit Contact](https://www.cynbit.in/contact)
- [Cynbit Careers](https://www.cynbit.in/careers)

These pages provide publicly available context for the prototype; they are not independent verification of internal company capabilities.

## Disclaimer

This is an independent assessment prototype exploring a potential AI-assisted business workflow. It is not an official Cynbit product and does not imply access to confidential company information or endorsement by Cynbit.

## Author

**Gourav Chhatwani**

- GitHub: [GouravGC](https://github.com/GouravGC)
- Portfolio: [Data Science & AI Portfolio](https://gcsportfolio.streamlit.app/)
- Live Project: [Cynbit AI Opportunity Blueprint Copilot](https://cynbit-ai-opportunity-copilot.streamlit.app/)

---

If you find this project useful, feel free to explore the source code and try the live demo.
