from fastapi import FastAPI

from .article_service import ArticleGenerator
from .activation import action_metrics
from .composite import ResearchSnapshot
from .history import ResearchHistory
from .render import render_spec_to_png
from .sources import sample_sources


app = FastAPI()

history = ResearchHistory()


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
    action_metrics.register_prompt("example-user")
    return example


@app.post("/research/snapshot")
def research_snapshot(prompt: str, user_id: str):
    action_metrics.register_prompt(user_id)
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
    snapshot = ResearchSnapshot(
        prompt=prompt,
        generated_at=datetime.utcnow(),
        article=article,
        infographic=InfographicSpec(
            title=infographic_spec["title"],
            generated_at=datetime.fromisoformat(infographic_spec["generated_at"]),
            infographic_type=infographic_spec["infographic_type"],
            citations=[Citation(**citation) for citation in infographic_spec["citations"]],
            layout_blocks=[LayoutBlock(**block) for block in infographic_spec["layout_blocks"]],
        ),
        sources=sources,
        confidence_score=0.83,
        ai_generated_label=True,
    )
    history.add(prompt, snapshot)
    return {
        "snapshot": snapshot,
        "infographic_png": png_bytes.hex(),
    }


@app.post("/activation/register_signin")
def register_signin(user_id: str):
    action_metrics.register_sign_in(user_id)
    return {"status": "signed_in"}


@app.get("/activation/report")
def activation_report():
    report = action_metrics.report()
    return report
