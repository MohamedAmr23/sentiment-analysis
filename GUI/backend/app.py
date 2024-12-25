from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import spacy

# Load the trained model and vectorizer
model = pickle.load(open('sentiment_model.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

# Load SpaCy for text preprocessing
nlp = spacy.load("en_core_web_sm")

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Preprocessing function
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    feedback = data['feedback']
    
    # Preprocess the feedback
    cleaned_feedback = preprocess_text(feedback)
    
    # Vectorize the feedback
    vectorized_feedback = vectorizer.transform([cleaned_feedback])
    
    # Predict sentiment
    prediction = model.predict(vectorized_feedback)[0]
    sentiment = "Positive" if prediction == 1 else "Negative"
    
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
