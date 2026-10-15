from pathlib import Path
import json


SOURCE_FILE = Path("data/public_sources/cynbit_sources.json")


def test_public_sources_exist():
    assert SOURCE_FILE.exists()


def test_public_sources_have_urls_and_text():
    sources = json.loads(SOURCE_FILE.read_text(encoding="utf-8"))

    assert len(sources) >= 1

    for source in sources:
        assert source["url"].startswith("https://")
        assert len(source["text"].strip()) > 0


def test_required_source_pages_are_present():
    sources = json.loads(SOURCE_FILE.read_text(encoding="utf-8"))
    urls = {source["url"] for source in sources}

    assert any("/services" in url for url in urls)
    assert any("/contact" in url for url in urls)
    assert any("/careers" in url for url in urls)


def test_blueprint_has_required_sections():
    from app.workflows.blueprint import create_blueprint
    from unittest.mock import patch

    mock_output = """
    1. Business objective
    2. Extracted requirements
    3. Relevant Cynbit services with supporting URLs
    4. Proposed architecture and why it fits
    5. Missing questions
    6. Risks and safeguards
    7. Implementation phases
    8. Evaluation metrics
    9. Assumptions and limitations
    """

    with patch(
        "app.workflows.blueprint.generate_response",
        return_value=mock_output,
    ):
        result = create_blueprint("Classify and route customer enquiries.")

    required_sections = [
        "Business objective",
        "Extracted requirements",
        "Relevant Cynbit services",
        "Proposed architecture",
        "Missing questions",
        "Risks and safeguards",
        "Implementation phases",
        "Evaluation metrics",
        "Assumptions and limitations",
    ]

    for section in required_sections:
        assert section.lower() in result.lower()


def test_blueprint_includes_source_grounding_safeguard():
    from app.workflows.blueprint import create_blueprint
    from unittest.mock import patch

    mock_output = (
        "Relevant Cynbit services: AI automation. "
        "Source: https://www.cynbit.in/services"
    )

    with patch(
        "app.workflows.blueprint.generate_response",
        return_value=mock_output,
    ):
        result = create_blueprint("Automate customer enquiries.")

    assert "https://www.cynbit.in/services" in result


def test_blueprint_includes_human_review_safeguard():
    from app.workflows.blueprint import create_blueprint
    from unittest.mock import patch

    mock_output = (
        "Uncertain classifications must be reviewed by a human "
        "before routing or taking action."
    )

    with patch(
        "app.workflows.blueprint.generate_response",
        return_value=mock_output,
    ):
        result = create_blueprint("Route customer enquiries.")

    assert "human" in result.lower()
    assert "review" in result.lower()
