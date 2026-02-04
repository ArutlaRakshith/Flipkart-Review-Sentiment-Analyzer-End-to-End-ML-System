
# Flipkart Review Sentiment Analyzer (End-to-End ML System)

This project is an end-to-end sentiment analysis system for Flipkart product reviews. The goal of this project is to analyze customer reviews and predict whether the sentiment is positive or negative using machine learning. The system includes data preprocessing, model training, real-time inference using FastAPI, and a simple Streamlit web interface for user interaction.

---

## What This Project Does

- Takes a product review as input from the user  
- Sends the review text to a FastAPI backend  
- The backend loads a trained ML model and predicts the sentiment  
- The predicted sentiment and confidence score are sent back  
- The Streamlit UI displays the result to the user in real time  
---


## Features

- Data cleaning and preprocessing of real-world Flipkart reviews  
- Text feature extraction using TF-IDF  
- Machine learning model training and evaluation (Logistic Regression)  
- Real-time sentiment prediction API using FastAPI  
- Simple web UI built with Streamlit  
- End-to-end ML workflow from data to deployment  

---

##  Tech Stack

- **Language:** Python  
- **ML & NLP:** scikit-learn, TF-IDF, Logistic Regression  
- **Backend API:** FastAPI  
- **Frontend UI:** Streamlit  
- **Data Handling:** pandas, numpy  
- **Model Saving:** joblib  
- **Deployment:** AWS EC2  

---

## 📂 Project Structure


---

## 🔄 How the System Works (Flow)

1. The user enters a review in the Streamlit web page.  
2. Streamlit sends the review text to the FastAPI `/predict` endpoint.  
3. FastAPI loads the trained ML model and runs prediction on the input text.  
4. The API returns the sentiment label (positive/negative) and confidence score.  
5. Streamlit displays the result to the user in a friendly format.


---

## 📊 Dataset

The dataset contains Flipkart product reviews with ratings and short review summaries.  
Ratings are converted into sentiment labels:

- Rating ≥ 4 → Positive  
- Rating ≤ 2 → Negative  
- Neutral ratings are ignored for binary classification.

  ---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd flipkart-sentiment-mlops
```
- pip install -r requirements.txt
- Train the model
    python src/train.py
    This will create the trained model file
      model/sentiment_model.joblib
- Run FastAPI Backend
```
      uvicorn api.app:app --reload
      http://127.0.0.1:8000/docs ( Open Swagger UI )
```
  You can test the API by sending a review text to the /predict endpoint.
  
- Run Streamlit UI
  ```
      streamlit run ui/app.py
      http://localhost:8501
  ```
  Enter any review text and click Analyze Sentiment to get the prediction.
  
