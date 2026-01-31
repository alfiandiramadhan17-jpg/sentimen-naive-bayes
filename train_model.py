from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

def train_and_evaluate(X, y):
    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    X_tfidf = vectorizer.fit_transform(X)

    # Split data 80% training, 20% testing
    X_train, X_test, y_train, y_test = train_test_split(
        X_tfidf, y, test_size=0.2, random_state=42, stratify=y
    )

    # Model Naive Bayes
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Prediksi
    y_pred = model.predict(X_test)

    # Evaluasi
    print("=== CLASSIFICATION REPORT ===")
    print(classification_report(y_test, y_pred))

    print("=== CONFUSION MATRIX ===")
    print(confusion_matrix(y_test, y_pred))

    return model, vectorizer
