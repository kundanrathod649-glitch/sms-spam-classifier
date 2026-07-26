import streamlit as st
import pickle
import preprocess

@st.cache_resource()
def load_model():
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return vectorizer, model

vectorizer, model = load_model()

def set_page_config():
    st.title("SMS Spam Classifier")
    page_icon = "🚨"
    layout = "centered"

st.title("SMS Spam Detector")
st.subheader("This is a simple web application that uses a machine learning model to classify SMS messages as spam or not spam.")

message = st.text_area("Enter your SMS message here:",placeholder="Example: Congratulations! You won a free iPhone...")

if st.button("🕵🏻‍♀️ Predict"):
    if message:
        processed_message = preprocess.trans_SMS(message)
        vectorized_message = vectorizer.transform([processed_message])
        prediction = model.predict(vectorized_message)
        if prediction[0] == 1:
            st.error("🚨 This message is SPAM.")
        else:
            st.success("✅ This message is NOT SPAM.")