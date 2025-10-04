import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Setup ---
st.set_page_config(page_title="Feedback Dashboard", layout="wide")
st.title("Customer Feedback Analysis Dashboard 📊")

# --- Load Data ---
# Load the main results file
df_results = pd.read_csv('test_results.csv')
# Load the topic modeling results
df_topics = pd.read_csv('topics.csv')

# --- Sidebar Filters ---
st.sidebar.header("Filter Reviews")
sentiment_filter = st.sidebar.selectbox(
    "Filter by Predicted Sentiment",
    options=["All", "positive", "neutral", "negative"],
    index=0  # Default to "All"
)

# --- Main Page ---

# Filter the DataFrame based on the sidebar selection
if sentiment_filter != "All":
    filtered_df = df_results[df_results['predicted_sentiment'] == sentiment_filter]
else:
    filtered_df = df_results

# --- Display Key Metrics ---
st.subheader("Key Metrics")
col1, col2 = st.columns(2)
col1.metric("Total Reviews Analyzed (Test Set)", len(filtered_df))
col2.metric("Sentiment Model Accuracy", "83.00%") # Your actual accuracy

# --- Display Charts and Data ---
col1, col2 = st.columns(2)

with col1:
    # Display Sentiment Distribution Chart
    st.subheader("Sentiment Distribution")
    sentiment_counts = df_results['predicted_sentiment'].value_counts()
    fig = px.bar(
        sentiment_counts,
        x=sentiment_counts.index,
        y=sentiment_counts.values,
        title="Count of Reviews by Sentiment",
        labels={'x': 'Sentiment', 'y': 'Number of Reviews'}
    )
    st.plotly_chart(fig)

with col2:
    # Display Topic Modeling Results
    st.subheader("Top Topics Discovered")
    st.dataframe(df_topics.head(10)) # Display top 10 topics

# Display the filtered reviews table at the bottom
st.subheader("Filtered Reviews")
st.dataframe(filtered_df)