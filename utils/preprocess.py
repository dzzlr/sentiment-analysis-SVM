import re

def clean_from_tweet(text):
    text = re.sub(r"RT", ' ', text)
    text = re.sub(r"@[A-Za-z0-9]+", ' ', text)
    text = re.sub(r"#[A-Za-z0-9]+", ' ', text)
    text = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", ' ', text)
    text = re.sub(r"[^\w\s]", ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    text = text.lower()
    text = text.split()
    return text
