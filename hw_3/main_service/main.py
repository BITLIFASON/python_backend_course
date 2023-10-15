import uvicorn
from fastapi import FastAPI
import requests

app = FastAPI(
    title="Main Service",
    description="Homework for the ITMO course Python Backend",
    contact={"name": "BITLIFASON", "url": "https://github.com/BITLIFASON"},
    version="0.0.1",
    docs_url="/docs",
)


@app.get("/analysis/")
async def get_analysis(text: str) -> str:
    """
    Analyzes topic and the sentiment of text

    - Args:
        - data : input text

    - Returns:
        - str : text description
    """
    sent_text = requests.post('http://sentiment_service:8002/sentiment/', json={"text": text}).json() # http://sentiment_service:8002/sentiment/ http://127.0.0.1:8002/sentiment/
    class_text = requests.post('http://classification_service:8003/classification/', json={"text": text}).json() # http://classification_service:8003/classification/ http://127.0.0.1:8003/classification/
    return f'This {sent_text} text about {class_text}'


if __name__ == "__main__":

    host = "0.0.0.0"
    port = 8001
    uvicorn.run(app, host=host, port=port)