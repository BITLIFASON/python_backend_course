import uvicorn
from fastapi import FastAPI

from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer

pt_save_directory = "Yueh-Huan/news-category-classification-distilbert"
# pt_save_directory = "class_model"
model = AutoModelForSequenceClassification.from_pretrained(pt_save_directory, from_tf=True) # from_tf=True
tokenizer = AutoTokenizer.from_pretrained(pt_save_directory)

app = FastAPI(
    title="Classification Service",
    description="Homework for the ITMO course Python Backend",
    contact={"name": "BITLIFASON", "url": "https://github.com/BITLIFASON"},
    version="0.0.1",
    docs_url="/docs",
)

classes = ['PARENTS',
     'WELLNESS',
     'PARENTING',
     'COMEDY',
     'POLITICS',
     'BLACK VOICES',
     'QUEER VOICES',
     'ENTERTAINMENT',
     'CULTURE & ARTS',
     'TECH',
     'RELIGION',
     'STYLE & BEAUTY',
     'HEALTHY LIVING',
     'TRAVEL',
     'GREEN',
     'IMPACT',
     'BUSINESS',
     'DIVORCE',
     'SCIENCE',
     'SPORTS',
     'LATINO VOICES',
     'WORLD NEWS',
     'HOME & LIVING',
     'MEDIA',
     'U.S. NEWS',
     'TASTE',
     'FOOD & DRINK',
     'WEIRD NEWS',
     'STYLE',
     'WOMEN',
     'ARTS & CULTURE',
     'CRIME',
     'MONEY',
     'WEDDINGS',
     'ARTS',
     'WORLDPOST',
     'THE WORLDPOST',
     'EDUCATION',
     'COLLEGE',
     'GOOD NEWS',
     'FIFTY',
     'ENVIRONMENT']


@app.post("/classification/")
async def get_class(data: dict) -> str:
    """
    Predict class of text

    - Args:
        - data : json with text

    - Returns:
        - str : class name
    """
    token_text = tokenizer(data['text'], return_tensors="pt")
    model_output = model(**token_text).logits.argmax()
    cls = classes[model_output].lower()
    return cls


if __name__ == "__main__":

    host = "0.0.0.0"
    port = 8003
    uvicorn.run(app, host=host, port=port)