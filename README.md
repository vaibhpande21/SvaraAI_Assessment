# 📧 Email Reply Sentiment Classifier

This project classifies email replies into **positive**, **neutral**, or **negative** categories using both **classical ML models (Logistic Regression, LightGBM)** and **Transformers (distilbert-base-uncased)**.  

It includes:  
- Full **ML/NLP pipeline** (preprocessing → modeling → evaluation)  
- **Model comparison & selection**  
- **Deployment** via Flask API  
- **Docker support** for easy containerized deployment  

---

## 📊 Model Comparison

| Model                  | Accuracy | Macro F1 | Pros ✅ | Cons ⚠️ |
|-------------------------|----------|----------|--------|---------|
| Logistic Regression (TF-IDF) | **0.981** | **0.981** | Fast, lightweight, easy to retrain/deploy | Linear, may miss complex context |
| LightGBM (TF-IDF)      | 0.980    | 0.980    | Handles non-linearities, robust | Slightly heavier, no real gain here |
| distilbert-base-uncased (Transformer)  | 0.995    | 0.995    | Captures semantic nuance, best accuracy | Heavier to train/deploy |

👉 **Production Choice:** Logistic Regression, due to its **98%+ accuracy, simplicity, and speed**. distilbert-base-uncased is considered if the dataset grows or text becomes more nuanced.  

---

## 🚀 Running the Project

### 1️⃣ Local Setup
```bash
# Clone repo
git clone <your-repo-url>
cd SvaraAI_Assessment

# Create virtual env
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt
```
---

### 2️⃣ Start the Flask API

- load best model, vectorixer and label encoder
```bash
python text_class.py
```
The API will start at:
```bash
http://127.0.0.1:5005/predict
```
---

## 🌐 Web API Development
- **File:** `text_class.py`
- Endpoints:
  - `/predict` → Accepts JSON input and returns label and confidence
- Example Request:
  ```json
  {
   "text" : "Sorry, we are not interested at the moment."
  } 
   ```
- Example Response:
  ```json
  {
       "confidence": 0.5769357408749977,
       "label": "negative"
  } 
   ```

  ## 🐳 Containerization
- **Dockerfile:**
  - Installs dependencies.
  - Runs Flask API container.
- **requirements.txt** ensures consistent environments.

---

## 📂 Project Structure  
```plaintext
SvaraAI_Assessment/
│── app.py                             # Flask API
│── assessment_SvaraAI_cleaned.ipynb   # Full ML/NLP pipeline notebook
│── requirements.txt                   # Dependencies
│── Dockerfile                         # Docker build file
│── logreg_model.pkl                   # Saved Logistic Regression model
│── tfidf_vectorizer.pkl               # Saved TF-IDF vectorizer
│── label_encoder.pkl                  # Saved label encoder


```
---
  

