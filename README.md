# Cynbit AI Opportunity Blueprint Copilot

An AI-powered proof of concept developed for the **Cynbit AI/ML Engineer Intern Technical Assessment**. The application explores AI/ML business opportunities and demonstrates AI-assisted customer enquiry classification, triage, and solution planning.

## Project Links

- **Live Demo:** https://cynbit-ai-opportunity-copilot.streamlit.app/
- **GitHub Repository:** https://github.com/GouravGC/cynbit-ai-opportunity-copilot
- **AI Opportunity Report:** [AI_OPPORTUNITY_REPORT.md](AI_OPPORTUNITY_REPORT.md)
- **Technical Approach Report:** [TECHNICAL_APPROACH.md](TECHNICAL_APPROACH.md)

## Overview

Businesses receive enquiries that require manual interpretation, qualification, prioritisation, and coordination between teams. AI can help structure this information and recommend appropriate next steps, reducing repetitive work while keeping people responsible for decisions.

This project demonstrates two complementary workflows:

1. **Opportunity Blueprint:** Converts a business inquiry into a structured AI solution proposal using retrieved public website evidence.
2. **Enquiry Classification & Routing:** Analyses a customer enquiry, identifies its intent, recommends a service category and destination team, and highlights missing information.

The project recommends AI-powered customer enquiry classification and lead routing as a potential pilot opportunity. The recommendation requires validation with business stakeholders and representative data.

## Features

### 1. Opportunity Blueprint

The blueprint workflow:

- Accepts a business inquiry describing a problem, goals, requirements, and constraints.
- Retrieves relevant public-source evidence using TF-IDF similarity.
- Uses an LLM to generate a structured AI solution proposal.
- Identifies potentially relevant Cynbit services and supporting source URLs.
- Separates publicly advertised services from proposed solution architecture.
- Outlines implementation phases, risks, safeguards, evaluation metrics, and unanswered questions.
- Allows the generated blueprint to be downloaded as a Markdown file.

### 2. AI-Powered Customer Enquiry Classification

The classification workflow:

- Accepts a customer enquiry or a sample query.
- Identifies the enquiry's intent and generates a factual summary.
- Assigns a service category.
- Estimates qualitative urgency and confidence.
- Recommends a destination team and next action.
- Identifies missing information that may require clarification.
- Displays the results and supports downloading the structured classification.

**Important:** Both workflows are separate actions in the application. Users can copy an inquiry from one tab and paste it into the other when testing the two workflows together.

## Technology Stack

- **Language:** Python
- **Application UI:** Streamlit
- **LLM integration:** OpenAI-compatible client through OpenRouter
- **Language model:** Google Gemini 2.5 Flash, accessed through OpenRouter
- **Retrieval:** Scikit-learn TF-IDF vectorization and cosine similarity
- **Configuration:** Environment variables and `python-dotenv`
- **Testing:** Pytest

## Architecture

### Opportunity Blueprint Workflow

1. The user submits a business inquiry.
2. The retriever loads the collected public-source dataset.
3. Text is divided into overlapping chunks and ranked using TF-IDF similarity.
4. Relevant evidence and source URLs are added to the LLM prompt.
5. The LLM generates a structured opportunity blueprint.
6. The user reviews and downloads the result.

### Enquiry Classification Workflow

1. The user enters or loads a customer enquiry.
2. The LLM analyses the enquiry and returns structured JSON.
3. The application validates the output and applies safe defaults to unsupported category, urgency, or confidence values.
4. The application displays the classification, suggested route, recommended next action, and missing information.
5. The user reviews the recommendations before acting on them.

## Getting Started

### Prerequisites

- Python 3.11 recommended
- Git
- An OpenRouter API key with access to the configured model

### 1. Clone the repository

```bash
git clone https://github.com/GouravGC/cynbit-ai-opportunity-copilot.git
cd cynbit-ai-opportunity-copilot
```

### 2. Create and activate a Conda environment

```bash
conda create -n cynbit_proj python=3.11 -y
conda activate cynbit_proj
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Replace the placeholder with your own API key. Never commit `.env` or expose API keys in screenshots, logs, or public files.

### 5. Run the application

```bash
streamlit run app/ui.py
```

Open the local URL printed by Streamlit in your browser.

## Testing

Run the available automated tests:

```bash
python -m pytest -v
```

Manual testing should include:

- Generating a blueprint from a detailed business inquiry.
- Checking whether relevant source URLs appear in the blueprint.
- Classifying a short customer enquiry.
- Testing an ambiguous or incomplete enquiry.
- Checking the displayed missing-information recommendations.
- Verifying that the application handles invalid inputs and API errors appropriately.

Example outputs should be treated as functional demonstrations, not evidence of measured classification accuracy.

## Assessment Deliverables

### 1. AI Opportunity Report

`AI_OPPORTUNITY_REPORT.md` analyses potential business applications of AI/ML and presents a proposed opportunity for further investigation.

### 2. AI/ML Proof of Concept

The Streamlit application demonstrates evidence-informed opportunity blueprint generation and AI-assisted customer enquiry classification and routing recommendations.

### 3. Technical Approach Report

`TECHNICAL_APPROACH.md` describes the architecture, model integration, retrieval approach, implementation plan, safeguards, and proposed evaluation methodology.

## Responsible AI and Limitations

- The application is a proof of concept, not a production customer-management system.
- Classification, urgency, confidence, and routing recommendations are generated by an LLM and may be incorrect.
- Confidence is qualitative and is not a calibrated probability.
- The application does not contact customers, update a CRM, or execute actual routing actions.
- Public-source retrieval can return incomplete or irrelevant evidence.
- Source URLs should be checked to confirm that they support the associated claims.
- No classification accuracy or business performance improvement should be claimed without a documented evaluation.
- Human review is required before acting on generated recommendations.
- Production deployment would require representative labelled data, evaluation, privacy controls, monitoring, and stakeholder approval.

## Future Improvements

Potential next steps, subject to validation and project requirements:

- Evaluate classification and routing recommendations against a labelled enquiry dataset.
- Measure category precision and recall, routing agreement, human correction rate, latency, and inference cost.
- Improve missing-information detection and structured-output validation.
- Explore approved CRM integration and controlled routing only after the prototype has been evaluated.
- Add monitoring and feedback mechanisms for continuous improvement.

## Author

**Gourav Chhatwani**

GitHub: https://github.com/GouravGC

Portfolio: https://gcsportfolio.streamlit.app/

---

*Developed as an AI/ML internship assessment proof of concept. Business opportunities and proposed architectures are recommendations for further evaluation, not claims of existing production capabilities.*