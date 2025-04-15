import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import random

# Set Streamlit page config FIRST
st.set_page_config(page_title="Score Predictor", page_icon="✨", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        body {
            background-color: #fff0f5;
            font-family: 'Segoe UI', sans-serif;
        }

        .stApp {
            background-color: #fff0f5;
        }

        h1, h3, h4 {
            color: #ff69b4;
        }

        .block-container {
            padding: 2rem 2rem;
            border-radius: 25px;
            background-color: #ffffff;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
        }

        .css-1offfwp {
            background-color: #fff0f5;
        }

        .stButton > button {
            background-color: #ff69b4;
            color: white;
            border-radius: 10px;
            padding: 10px 16px;
            font-size: 16px;
        }

        .stSlider > div {
            background-color: #ffe6ec;
        }

        .stTextInput > div > input {
            background-color: #ffe6ec;
            color: black;
            border-radius: 8px;
        }

        .stNumberInput input {
            background-color: #ffe6ec;
            color: black;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Train a simple model
X = np.array([[1], [2], [3], [4], [5], [6], [7]])
y = np.array([30, 40, 50, 60, 65, 75, 85])
model = LinearRegression()
model.fit(X, y)

# Cute quotes + tips
quotes = [
    "Believe you can and you're halfway there.",
    "Small progress is still progress.",
    "Don’t stress. Do your best. Forget the rest.",
    "Study like your dreams depend on it—because they do!"
]

study_tips = {
    "math": "🔢 Focus on formulas and do lots of practice problems.",
    "science": "🧪 Understand the concepts and do quick concept maps.",
    "history": "📚 Use timelines, charts & flashcards.",
    "english": "✍️ Read articles, write essays, and brush up grammar.",
    "default": "📖 Break study into chunks and use the Pomodoro method."
}

# Header
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>🎓 Student Score Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Your magical study buddy to predict your score and motivate you!</p>", unsafe_allow_html=True)
st.markdown("---")

# Layout: split into two columns
col1, col2 = st.columns(2)

with col1:
    subject = st.text_input("📘 Subject", placeholder="Eg: Math, History").lower()

with col2:
    total_score = st.number_input("🧾 Total Exam Score", min_value=1, max_value=1000, value=100)

hours = st.slider("⏰ How many hours have you studied?", 0.0, 20.0, 1.0, 0.5)
target_score = st.number_input("🎯 Your Goal Score (Optional)", min_value=0.0, max_value=float(total_score), value=0.0)

# Prediction area
if st.button("✨ Predict My Score!"):
    predicted = model.predict([[hours]])[0]
    scaled = (predicted / 100) * total_score
    scaled = max(0, min(scaled, total_score))

    st.markdown(f"<h3 style='color: #00C9A7;'>📊 Your predicted score for <i>{subject or 'the subject'}</i> is <b>{scaled:.2f} / {total_score}</b></h3>", unsafe_allow_html=True)

    if target_score > 0:
        req_raw = (target_score / total_score) * 100
        needed_hours = (req_raw - model.intercept_) / model.coef_[0]
        needed_hours = max(0, needed_hours)
        st.info(f"📚 You may need to study about **{needed_hours:.1f} hours** to reach your goal of {target_score}.")

    tip = study_tips.get(subject, study_tips["default"])
    st.markdown(f"### 📝 Study Tip for You:\n{tip}")
    st.success(f"💖 *Motivation:* “{random.choice(quotes)}”")

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Created with love by Hiba • Student Edition</p>", unsafe_allow_html=True)
