import pandas as pd
from preprocessing import clean_text
from train_model import train_and_evaluate

# Load dataset
data = pd.read_csv("dataset_sentimen.csv")

# Pastikan kolom sesuai
if list(data.columns) != ["review_text", "sentiment"]:
    data.columns = ["review_text", "sentiment"]

# Preprocessing teks
data["clean_text"] = data["review_text"].astype(str).apply(clean_text)

X = data["clean_text"]
y = data["sentiment"]

# Training & evaluasi model
model, vectorizer = train_and_evaluate(X, y)

print("\nModel Naive Bayes berhasil dilatih.")
