
import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


SOURCE_FILE = Path("data/public_sources/cynbit_sources.json")


def retrieve_context(query: str, top_k: int = 5) -> str:
    sources = json.loads(SOURCE_FILE.read_text(encoding="utf-8"))

    chunks = []

    for source in sources:
        text = source["text"]
        start = 0

        while start < len(text):
            chunk = text[start:start + 700].strip()

            if chunk:
                chunks.append({
                    "url": source["url"],
                    "text": chunk,
                })

            start += 550

    if not chunks:
        return "No public source evidence was found."

    documents = [chunk["text"] for chunk in chunks]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
    )

    matrix = vectorizer.fit_transform(documents)
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, matrix).flatten()

    ranked_indices = scores.argsort()[::-1]
    results = []

    for index in ranked_indices:
        if scores[index] <= 0:
            continue

        chunk = chunks[index]
        results.append(
            f"Source URL: {chunk['url']}\n"
            f"Relevance score: {scores[index]:.3f}\n"
            f"Evidence: {chunk['text']}"
        )

        if len(results) >= top_k:
            break

    if not results:
        return "No relevant public evidence found. Do not invent company capabilities."

    return "\n\n---\n\n".join(results)
