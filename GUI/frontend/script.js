// script.js
document.getElementById('submitBtn').addEventListener('click', async () => {
    const feedback = document.getElementById('feedback').value;
    
    if (!feedback.trim()) {
        alert('Please enter your feedback!');
        return;
    }

    // Call the backend API
    const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ feedback: feedback }),
    });

    const data = await response.json();
    document.getElementById('result').textContent = `Sentiment: ${data.sentiment}`;
});
