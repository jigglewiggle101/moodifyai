from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import cv2
from keras.models import load_model
import numpy as np
from diary_model import analyze_diary

app = Flask(__name__)
CORS(app)

# Load emotion detection model
emotion_model = load_model('emotion_model.h5')  # Replace with your model
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Beatoven.ai API credentials
BEATOVEN_API_KEY = "your_beatover_api_key"
BEATOVEN_BASE_URL = "https://api.beatover.ai/music"

@app.route('/detect-emotion', methods=['POST'])
def detect_emotion():
    file = request.files['image']
    img_array = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    if len(faces) == 0:
        return jsonify({"error": "No face detected"})

    x, y, w, h = faces[0]
    roi_gray = gray[y:y + h, x:x + w]
    roi_gray = cv2.resize(roi_gray, (48, 48)) / 255.0
    roi_gray = np.expand_dims(np.expand_dims(roi_gray, axis=0), axis=-1)

    emotion_prediction = emotion_model.predict(roi_gray)
    emotion_label = emotion_labels[np.argmax(emotion_prediction)]

    return jsonify({"emotion": emotion_label})


@app.route('/analyze-diary', methods=['POST'])
def analyze_diary_text():
    data = request.json
    diary_text = data.get('text', '')

    if not diary_text:
        return jsonify({"error": "Diary text is empty"}), 400

    mood = analyze_diary(diary_text)  # NLP-based analysis
    return jsonify({"mood": mood})


@app.route('/get-playlist', methods=['POST'])
def get_playlist():
    data = request.json
    emotion = data.get('emotion', 'Neutral')
    diary_mood = data.get('diaryMood', 'balanced')

    # Map emotion + diary mood to Beatoven's mood
    emotion_to_mood = {
        ('Happy', 'positive'): 'energetic',
        ('Sad', 'negative'): 'calm',
        ('Angry', 'neutral'): 'intense',
        ('Neutral', 'positive'): 'balanced',
        ('Neutral', 'negative'): 'ambient',
    }
    mood = emotion_to_mood.get((emotion, diary_mood), 'balanced')

    headers = {'Authorization': f'Bearer {BEATOVEN_API_KEY}'}
    params = {'mood': mood, 'length': 10}
    response = requests.get(BEATOVEN_BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch playlist"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
