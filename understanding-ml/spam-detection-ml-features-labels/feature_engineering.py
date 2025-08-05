import pandas as pd

def extract_features(df: pd.DataFrame):
    keywords = ["win", "free", "offer", "prize"]

    def keyword_freq(text):
        text = text.lower()
        return sum(text.count(word) for word in keywords)

    df["keyword_count"] = df["email"].apply(keyword_freq)
    df["email_length"] = df["email"].apply(len)

    X = df[["keyword_count", "email_length"]]
    y = df["label"]

    return X, y
