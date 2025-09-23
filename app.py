from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load artifacts
model = joblib.load("logreg_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Initialize Flask app
app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    text = data.get("text", "")

    # Vectorize
    X = vectorizer.transform([text])

    # Predict
    probs = model.predict_proba(X)[0]
    pred_idx = np.argmax(probs)
    pred_label = label_encoder.inverse_transform([pred_idx])[0]

    return jsonify({"label": pred_label, "confidence": float(probs[pred_idx])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
