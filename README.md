# 📩 SMS Spam Detection using Machine Learning

A Machine Learning web application that detects whether an SMS message is **Spam** or **Not Spam**. The project is built using **Python, Scikit-learn, NLTK, and Streamlit**.

---

## 🚀 Live Demo

🔗 https://sms-spam-classifier-kundan.streamlit.app

---

## 📌 Features

- Detects Spam and Ham (Not Spam) SMS messages
- User-friendly Streamlit interface
- Text preprocessing using NLTK
- TF-IDF Vectorization
- Machine Learning based prediction
- Fast and lightweight deployment

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Pickle

---

## 📂 Project Structure

```
SMS-Spam-Classifier/
│
├── app.py
├── preprocess.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── spam.csv
├── SMS_spam.ipynb
├── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/kundanrathod649/sms-spam-classifier.git
```

```bash
cd sms-spam-classifier
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download NLTK Data

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 Machine Learning Workflow

1. Load SMS Dataset
2. Data Cleaning
3. Text Preprocessing
4. Tokenization
5. Remove Stopwords
6. Stemming
7. TF-IDF Vectorization
8. Model Training
9. Model Evaluation
10. Streamlit Deployment

---

## 📊 Model Pipeline

```
SMS Message
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorizer
      │
      ▼
Machine Learning Model
      │
      ▼
Spam / Not Spam
```

---

## 📈 Dataset

- SMS Spam Collection Dataset
- Contains Spam and Ham messages for binary classification.

---

## 🎯 Future Improvements

- Support multiple languages
- Confidence score
- Probability visualization
- Batch SMS prediction
- Upload CSV for bulk prediction

---

## 👨‍💻 Author

**Kundan Rathod**

- GitHub: https://github.com/kundanrathod649-glitch

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.