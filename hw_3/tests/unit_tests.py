import pytest
import requests


@pytest.mark.parametrize(
    "text, label",
    [
        ("A football coach has quit in England", "sports"),
        ("Investors reported a lack of changes in the market", "money"),
        ("Many hotels for tourists have opened in Turkey", "travel"),
    ],
)
def test_get_class(text, label):
    class_pred = requests.post(
        "http://localhost:8003/classification/", json={"text": text}
    ).json()
    assert class_pred == label


@pytest.mark.parametrize(
    "text, label",
    [
        ("A football coach has quit in England", "negative"),
        ("Investors reported a lack of changes in the market", "neutral"),
        ("Many hotels for tourists have opened in Turkey", "positive"),
    ],
)
def test_get_sentiment(text, label):
    sent_pred = requests.post(
        "http://localhost:8002/sentiment/", json={"text": text}
    ).json()
    assert sent_pred == label
