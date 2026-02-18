from fastapi import FastAPI

from .article_service import ArticleGenerator


app = FastAPI()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/articles/example")
def example_article(prompt: str):
    example = ArticleGenerator.create_example(prompt, sources=[
        "https://example.com/source-1",
        "https://example.com/source-2",
        "https://example.com/source-3",
    ])
    return example
