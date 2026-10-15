import json
from unittest.mock import patch

import pytest

from app.workflows.enquiry_router import (
    classify_enquiry,
    _extract_json,
)


def test_classification_returns_structured_result():
    mock_response = json.dumps({
        "category": "AI & Automation",
        "intent": "Qualify website leads",
        "summary": "Customer wants an AI chatbot integrated with a CRM.",
        "urgency": "medium",
        "suggested_route": "AI & Automation team",
        "next_action": "Confirm the CRM platform and lead volume.",
        "missing_information": ["Which CRM platform is used?"],
        "confidence": "high",
    })

    with patch(
        "app.workflows.enquiry_router.generate_response",
        return_value=mock_response,
    ):
        result = classify_enquiry(
            "We need a chatbot connected to our CRM."
        )

    assert result["category"] == "AI & Automation"
    assert result["urgency"] == "medium"
    assert result["human_review_required"] is True
    assert result["missing_information"] == [
        "Which CRM platform is used?"
    ]


def test_unknown_category_uses_safe_default():
    mock_response = json.dumps({
        "category": "Unknown Department",
        "intent": "Unclear",
        "summary": "Unclear request.",
        "urgency": "urgent",
        "suggested_route": "Manual review",
        "next_action": "Ask for clarification.",
        "missing_information": [],
        "confidence": "certain",
    })

    with patch(
        "app.workflows.enquiry_router.generate_response",
        return_value=mock_response,
    ):
        result = classify_enquiry("Can you help us?")

    assert result["category"] == "Other"
    assert result["urgency"] == "medium"
    assert result["confidence"] == "low"
    assert result["human_review_required"] is True


def test_empty_enquiry_is_rejected():
    with pytest.raises(ValueError):
        classify_enquiry("   ")


def test_markdown_fenced_json_is_parsed():
    result = _extract_json(
        '```json\n{"category": "Other"}\n```'
    )

    assert result["category"] == "Other"


def test_invalid_json_is_rejected():
    with pytest.raises((ValueError, json.JSONDecodeError)):
        _extract_json("This is not JSON")