<h1 style='text-align':'center'>Sentiment Analysis Web Application</h1>
Project Overview
This project is a complete end-to-end web application for Sentiment Analysis using machine learning. The application allows users to input feedback, processes it through a trained sentiment analysis model, and provides a classification as either positive or negative.

The application is designed with a user-friendly interface built with HTML, CSS, and JavaScript for the frontend, and a Flask backend for handling predictions using the machine learning model.

Features
Text Preprocessing:

Removal of HTML tags, special characters, and stopwords.
Conversion of text to lowercase for normalization.
Machine Learning Model:

A Logistic Regression model trained on the IMDb dataset of 50,000 movie reviews.
Utilizes the TF-IDF Vectorizer for feature extraction.
Interactive Web Interface:

Users can submit their feedback through a simple and intuitive form.
Real-time sentiment analysis results displayed as positive or negative.
Visualization:

Graphical representation of dataset distribution, word clouds for positive/negative reviews, and accuracy metrics.
Custom Stopword Removal:

A list of predefined stopwords ensures irrelevant words are excluded from the analysis.
Backend API:

Flask-based REST API for handling user input and predicting sentiment.
Tech Stack
Frontend:
HTML5
CSS3
JavaScript
Backend:
Flask (Python)
REST API integration
Machine Learning:
Scikit-learn (Logistic Regression, TF-IDF Vectorizer)
SpaCy for text preprocessing
Dataset
The model is trained on the IMDb Dataset of 50K Movie Reviews, sourced directly from Kaggle.


Installation Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/sentiment-analysis-webapp.git
cd sentiment-analysis-webapp
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Download the SpaCy language model:

bash
Copy code
python -m spacy download en_core_web_sm
Run the Flask backend:

bash
Copy code
python backend/app.py
Open the application in your browser:

Navigate to http://127.0.0.1:5000.

Usage
Enter your feedback in the input field.
Submit the form to analyze the sentiment of the feedback.
View the result as positive or negative on the screen.
Future Enhancements
Improve the accuracy of the machine learning model using deep learning techniques like LSTM.
Add more languages to the sentiment analysis.
Integrate additional visualizations to showcase predictions and performance metrics.
Deploy the application using cloud services like AWS or Heroku.

Screenshots
![Capture](https://github.com/user-attachments/assets/4666e13f-56e8-4f3c-8de7-5e2b59ec7a9f)
Contributing
Feel free to submit issues or pull requests to improve the project!
