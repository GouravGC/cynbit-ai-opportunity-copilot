
import json
from html.parser import HTMLParser
from pathlib import Path

import requests


URLS = [
    "https://www.cynbit.in/services",
    "https://www.cynbit.in/contact",
    "https://www.cynbit.in/careers",
]


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self.skip = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self.skip = False

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.text.append(data.strip())


def fetch_page(url):
    response = requests.get(
        url,
        timeout=20,
        headers={"User-Agent": "CynbitOpportunityCopilot/1.0"},
    )
    response.raise_for_status()

    parser = TextExtractor()
    parser.feed(response.text)

    return {
        "url": url,
        "text": " ".join(parser.text),
        "status": "fetched",
    }


def main():
    sources = []

    for url in URLS:
        try:
            source = fetch_page(url)
            sources.append(source)
            print(f"Fetched: {url}")
        except requests.RequestException as error:
            print(f"Failed: {url} — {error}")

    output = Path("data/public_sources/cynbit_sources.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(sources, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\nSaved {len(sources)} sources to {output}")


if __name__ == "__main__":
    main()
