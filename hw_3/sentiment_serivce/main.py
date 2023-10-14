import uvicorn
from fastapi import FastAPI

from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer

# model_id = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"
pt_save_directory = "sent_model"
model = AutoModelForSequenceClassification.from_pretrained(pt_save_directory)
tokenizer = AutoTokenizer.from_pretrained(pt_save_directory)

emotions = ['positive', 'neutral', 'negative']

app = FastAPI(
    title="Sentiment Service",
    description="Homework for the ITMO course Python Backend",
    contact={"name": "BITLIFASON", "url": "https://github.com/BITLIFASON"},
    version="0.0.1",
    docs_url="/docs",
)

@app.post("/sentiment/")
async def get_sentiment(data: dict) -> str:
    """
    Predict sentiment of text

    - Args:
        - data : json with text

    - Returns:
        - str : sentiment name
    """
    token_text = tokenizer(data['text'], return_tensors="pt")
    model_output = model(**token_text).logits.argmax()
    emotion = emotions[model_output]
    return emotion


if __name__ == "__main__":

    host = "0.0.0.0"
    port = 8002
    uvicorn.run(app, host=host, port=port)