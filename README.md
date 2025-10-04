Customer Feedback Analysis Dashboard 📊


This project is an end-to-end data science application that automatically analyzes customer feedback for a service like Zomato. It uses Natural Language Processing (NLP) to perform sentiment analysis and topic modeling, presenting the results in an interactive web dashboard built with Streamlit.


Key Features
Sentiment Analysis: Classifies customer reviews as positive, negative, or neutral with 83% accuracy using a pre-trained RoBERTa model.

Topic Modeling: Discovers key themes and topics within the reviews (e.g., "delivery time," "food quality," "app issues") using BERTopic.

Interactive Dashboard: A user-friendly web interface built with Streamlit to visualize key metrics, filter reviews, and explore the discovered topics.

Data Pipeline: A complete pipeline that fetches, cleans, processes, and analyzes data.

Tech Stack
Language: Python

Data Manipulation: Pandas, NumPy

NLP: Hugging Face Transformers, NLTK

Topic Modeling: BERTopic

Dashboard: Streamlit

Plotting: Plotly Express

ML Utilities: Scikit-learn

## How to Run Locally
To set up and run this project on your local machine, follow these steps.

### 1. Clone the Repository
Bash

git clone https://github.com/Arpit-saxena-2004/zomato_bert_analysis.git
cd your-repo-name
### 2. Create and Activate an Environment
It's recommended to use a virtual environment.

Bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
### 3. Install Dependencies
Install all the required libraries from the requirements.txt file.

Bash

pip install -r requirements.txt
### 4. Download NLTK Data
Run a simple Python command to download the necessary 'stopwords' package.

Python

import nltk
nltk.download('stopwords')
### 5. Run the Streamlit App
Launch the interactive dashboard.

Bash

streamlit run dashboard.py
Your dashboard should now be open and running in your web browser!

## Project by
Arpit Saxena
