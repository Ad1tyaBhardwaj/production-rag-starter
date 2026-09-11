# src/production_rag_starter/api/main.py

from fastapi import FastAPI

app = FastAPI(
    title="Production RAG Starter",
    version="0.1.0",
)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}