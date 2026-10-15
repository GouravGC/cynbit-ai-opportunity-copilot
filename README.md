# Cynbit AI Opportunity Blueprint Copilot

An AI-powered proof of concept that transforms client business inquiries into structured AI solution blueprints using publicly available information from Cynbit's website.

## Overview

Businesses often need to translate operational challenges into practical AI opportunities. This application helps structure that process by combining public company information, relevance-based retrieval, and an LLM to generate a draft solution blueprint for human review.

## Features

- Generates structured AI opportunity blueprints from client inquiries.
- Retrieves relevant company information using TF-IDF and cosine similarity.
- Uses publicly available Cynbit website content as contextual evidence.
- Includes source URLs for company-service claims.
- Outlines requirements, proposed architecture, implementation phases, risks, and evaluation metrics.
- Highlights missing information and the need for human review.
- Provides a Streamlit interface and downloadable Markdown reports.
- Includes automated tests for basic application behavior.

## Technical Architecture

1. **Data ingestion:** Collects publicly available Cynbit website pages.
2. **Text preparation:** Splits the collected text into overlapping chunks.
3. **Retrieval:** Uses TF-IDF vectorization and cosine similarity to identify relevant passages.
4. **Generation:** Sends the inquiry and retrieved evidence to Gemini 2.5 Flash through OpenRouter.
5. **Output:** Generates a structured blueprint for human review.

The current implementation uses lexical retrieval, not embedding-based semantic search or a dedicated vector database.

## Tech Stack

- Python 3.11
- Streamlit
- scikit-learn
- OpenAI Python SDK
- Gemini 2.5 Flash via OpenRouter
- python-dotenv
- pytest

## Setup

Clone the repository and enter the project directory:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd cynbit-ai-opportunity-copilot
```

Create and activate a Python environment, then install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```text
OPENROUTER_API_KEY=your_openrouter_api_key
```

Run the application:

```bash
python -m streamlit run app/ui.py
```

Run the tests:

```bash
python -m pytest -v
```

## Public Sources

- https://www.cynbit.in/services
- https://www.cynbit.in/contact
- https://www.cynbit.in/careers

## Evaluation

The existing automated tests cover source availability, required public pages, basic blueprint structure, source URL presence, and human-review wording. Model responses are mocked in relevant tests; passing tests do not independently establish factual accuracy or production-grade safety.

## Limitations

- Generated blueprints are drafts, not final implementation commitments.
- Public website content does not independently verify internal company capabilities.
- Retrieval quality depends on source-text quality and keyword overlap.
- Proposed integrations, costs, timelines, and performance must be validated.
- Human review is required before acting on recommendations.

## Disclaimer

This project is an assessment prototype demonstrating a potential AI-assisted business workflow. It does not represent an official Cynbit product or claim access to internal company information.