import streamlit as st
from transformers import pipeline
import pandas as pd

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# App title
st.title("Sentiment Analysis using BERT")
st.write("Enter one or more sentences (each sentence on a new line) to analyze their sentiment:")

# User input
user_input = st.text_area("Enter your text here (one sentence per line):")

# Star rating mapping
sentiment_labels = {
    "1 star": "⭐ (1 star) = Very Negative 😡",
    "2 stars": "⭐⭐ (2 stars) = Negative 😞",
    "3 stars": "⭐⭐⭐ (3 stars) = Neutral 😐",
    "4 stars": "⭐⭐⭐⭐ (4 stars) = Positive 🙂",
    "5 stars": "⭐⭐⭐⭐⭐ (5 stars) = Very Positive 😃"
}

# Example sentences
example_sentences = [
    "I love this place, it's amazing!",
    "The service was very bad.",
    "It's okay, nothing special.",
    "I'm extremely disappointed!",
    "This is the best experience I've ever had!"
]

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Try an Example"):
        user_input = "\n".join(example_sentences)
        st.text_area("Enter your text here (one sentence per line):", value=user_input, height=150, key="example")

with col2:
    if st.button("Clear Input"):
        user_input = ""
        st.text_area("Enter your text here (one sentence per line):", value=user_input, height=150, key="clear")

# Sentiment analysis
if st.button("Analyze Sentiment"):
    if user_input:
        sentences = user_input.split("\n")  # Split input into multiple sentences
        results = []
        
        for sentence in sentences:
            if sentence.strip():  # Ignore empty lines
                result = sentiment_pipeline(sentence)
                sentiment_label = result[0]['label']
                score = result[0]['score']
                
                # Convert label to integer for mapping
                star_rating = sentiment_label.split()[0]  # Extract the number
                sentiment_text = sentiment_labels.get(f"{star_rating} stars", "Unknown Sentiment")
                
                # Append result to list
                results.append([sentence, sentiment_text, f"{score:.2f}"])

        # Convert results to a DataFrame for better visualization
        df = pd.DataFrame(results, columns=["Original Text", "Sentiment", "Confidence Score"])
        st.subheader("Results:")
        st.dataframe(df, use_container_width=True)

    else:
        st.warning("Please enter text for analysis!")
