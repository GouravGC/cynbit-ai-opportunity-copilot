# Cynbit AI Opportunity Blueprint Copilot

**An AI-powered proof of concept for transforming business inquiries into evidence-grounded AI solution blueprints.**

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)](https://streamlit.io/)
[![Tests](https://img.shields.io/badge/Tests-6%20Passing-brightgreen)](https://docs.pytest.org/)

**Repository:** [GouravGC/cynbit-ai-opportunity-copilot](https://github.com/GouravGC/cynbit-ai-opportunity-copilot)

## Overview

Businesses need practical ways to translate operational challenges into actionable AI opportunities. This project demonstrates an AI-assisted workflow that takes a client inquiry, retrieves relevant information from Cynbit's publicly available website, and generates a structured solution blueprint for human review.

The prototype combines lightweight information retrieval, prompt engineering, and a large language model to support early-stage opportunity analysis and solution design.

## Key Features

- **Business inquiry analysis:** Converts natural-language problem descriptions into structured requirements.
- **Retrieval-augmented generation:** Retrieves relevant passages from collected public website content and supplies them as context to the language model.
- **Relevance-based search:** Uses TF-IDF vectorization, n-grams, and cosine similarity to rank relevant text chunks.
- **Evidence-aware recommendations:** Instructs the model to include source URLs for claims about publicly advertised services.
- **Structured solution blueprints:** Organizes outputs into business objectives, requirements, architecture, missing information, risks, implementation phases, and evaluation metrics.
- **Human-in-the-loop safeguards:** Highlights uncertainty, assumptions, and cases requiring human review.
- **Interactive application:** Provides a Streamlit interface for submitting inquiries and reviewing generated blueprints.
- **Report export:** Downloads generated blueprints as Markdown files.
- **Automated tests:** Includes tests for source availability and basic blueprint workflow behavior.

## How It Works

1. **Data ingestion:** Collects publicly available content from Cynbit's services, contact, and careers pages.
2. **Text chunking:** Splits the collected content into overlapping character-based chunks.
3. **Retrieval:** Applies TF-IDF vectorization and cosine similarity to retrieve relevant passages for a client inquiry.
4. **Prompt construction:** Combines the inquiry, retrieved evidence, source URLs, and output requirements.
5. **LLM generation:** Uses Gemini 2.5 Flash through the OpenRouter API to generate the blueprint.
6. **Presentation and export:** Displays the generated result in Streamlit and provides a Markdown download.

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
 TF-IDF Context Retrieval <---- Public Website Data
          |
          v
  Evidence-Aware Prompt
          |
          v
 Gemini 2.5 Flash via OpenRouter
          |
          v
 Structured Opportunity Blueprint
          |
          v
    Markdown Download
```

## Technology Stack

| Component | Technology |
|---|---|
| Language | Python 3.11 |
| User interface | Streamlit |
| Retrieval | scikit-learn, TF-IDF, cosine similarity |
| Language model | Gemini 2.5 Flash |
| LLM API integration | OpenAI Python SDK with OpenRouter |
| Configuration | python-dotenv |
| Testing | pytest |
| Version control | Git and GitHub |

## Blueprint Output

The generated report is structured around nine sections:

1. Business objective
2. Extracted requirements
3. Relevant Cynbit services with supporting URLs
4. Proposed architecture and rationale
5. Missing questions
6. Risks and safeguards
7. Implementation phases
8. Evaluation metrics
9. Assumptions and limitations

## Project Structure

```text
cynbit-ai-opportunity-copilot/
├── app/
│   ├── __init__.py
│   ├── llm_client.py
│   ├── main.py
│   ├── fetch_sources.py
│   ├── retriever.py
│   ├── ui.py
│   └── workflows/
│       ├── __init__.py
│       └── blueprint.py
├── data/
│   └── public_sources/
│       └── cynbit_sources.json
├── tests/
│   └── test_blueprint.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.11
- pip
- An OpenRouter API key with access to the selected model

### 1. Clone the repository

```bash
git clone https://github.com/GouravGC/cynbit-ai-opportunity-copilot.git
cd cynbit-ai-opportunity-copilot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Ensure `requirements.txt` includes all runtime dependencies, including the installed version of `scikit-learn`.

### 3. Configure the API key

Create a `.env` file in the project root:

```text
OPENROUTER_API_KEY=your_openrouter_api_key
```

Keep this file private. Never commit API keys or other secrets to GitHub.

### 4. Run the application

```bash
python -m streamlit run app/ui.py
```

### 5. Run automated tests

```bash
python -m pytest -v
```

## Evaluation and Testing

The current test suite contains six tests covering:

- Public source file availability and structure.
- Presence of required source pages.
- Basic blueprint output structure.
- Source URL presence.
- Human-review wording.

The workflow tests use mocked model responses. Passing these tests demonstrates basic application behavior, but does not independently prove the factual accuracy of generated recommendations, citation entailment, retrieval quality, or production-grade guardrail effectiveness.

## Current Limitations

- Retrieval uses lexical TF-IDF similarity rather than embedding-based semantic search.
- No dedicated vector database is used.
- Website extraction may retain some navigation or interface text.
- Public website statements are not independent verification of internal company capabilities.
- Model outputs may contain unsupported assumptions and require human review.
- Integrations, costs, timelines, and performance must be validated before implementation.
- This is a prototype, not a production deployment or a claim of measured business impact.

## Public Information Sources

The source collection is based on the following publicly accessible Cynbit pages:

- [Services](https://www.cynbit.in/services)
- [Contact](https://www.cynbit.in/contact)
- [Careers](https://www.cynbit.in/careers)

## Disclaimer

This project is an independent assessment prototype exploring a potential AI-assisted business workflow. It is not an official Cynbit product and does not imply access to confidential company information, confirmation of internal capabilities, or endorsement by Cynbit.

---

**Built by [Gourav Chhatwani](https://github.com/GouravGC)**