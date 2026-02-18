from fastapi import FastAPI

from .article_service import ArticleGenerator
from .composite import ResearchSnapshot
from .render import render_spec_to_png
from .sources import sample_sources


app = FastAPI()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/articles/example")
def example_article(prompt: str):
    example = ArticleGenerator.create_example(
        prompt,
        sources=[
            "https://example.com/source-1",
            "https://example.com/source-2",
            "https://example.com/source-3",
        ],
    )
    return example


@app.post("/research/snapshot")
def research_snapshot(prompt: str):
    sources = sample_sources(prompt)
    article = ArticleGenerator.create_example(prompt, sources=[source.source.url for source in sources])
    infographic_spec = {
        "title": f"Infographic for {prompt}",
        "generated_at": datetime.utcnow().isoformat(),
        "infographic_type": "timeline",
        "citations": [
            {"id": source.id, "title": source.source.title, "url": source.source.url, "publisher": source.source.publisher, "accessed_at": source.source.accessed_at.isoformat()}
            for source in sources
        ],
        "layout_blocks": [
            {"id": "block-1", "type": "text", "content": "Key takeaway", "citation_ids": [1]},
            {"id": "block-2", "type": "text", "content": "Supporting claim", "citation_ids": [2, 3]},
        ],
    }
    png_bytes = render_spec_to_png(infographic_spec)
    return {
        "prompt": prompt,
        "article": article,
        "infographic": infographic_spec,
        "sources": sources,
        "infographic_png": png_bytes.hex(),
    }
