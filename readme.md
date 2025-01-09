# Emotion-Based Music Playlist Generator

This project is an AI-powered application that generates personalized music playlists based on the user's facial expressions and diary reflections. The application uses computer vision for emotion detection, sentiment analysis for diary entries, and integrates with the Beatoven.ai API to fetch mood-specific playlists. The frontend includes dynamic visualizations using D3.js and Three.js, providing a responsive experience across web and mobile platforms.

---

## Features

- **Facial Expression Recognition**: Uses a pre-trained emotion detection model to identify the user's mood.
- **Diary Reflections**: Allows users to write daily reflections and analyzes sentiment to customize playlists further.
- **Beatoven.ai Integration**: Fetches mood-based playlists using the Beatoven.ai API.
- **Dynamic Visualizations**: Implements D3.js for 2D data visualization and Three.js for 3D interactive music visualization.
- **Responsive Design**: Fully responsive for desktop, tablet, and mobile.

---

## File Structure

### Backend
```
/backend
  ├── app.py            # Main Flask application
  ├── diary_model.py    # Diary sentiment analysis using NLTK
  ├── emotion_model.h5  # Pre-trained emotion detection model
  ├── requirements.txt  # Python dependencies
```

### Frontend
```
/frontend
  ├── src
      ├── components
          ├── App.jsx               # Main app
          ├── Diary.jsx             # Diary component
          ├── PlaylistVisualization.jsx # Playlist visualizations (D3.js & Three.js)
      ├── styles
          ├── styles.css            # Global styles
      ├── index.js                  # App entry point
  ├── package.json                  # Frontend dependencies
```

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

---

### Backend Setup

1. Navigate to the backend folder:
   ```bash
   cd /path/to/backend
   ```

2. Create a virtual environment (optional):
   ```bash
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   .\env\Scripts\activate # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. The backend will start at `http://localhost:5000`.

---

### Frontend Setup

1. Navigate to the frontend folder:
   ```bash
   cd /path/to/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

4. The frontend will start at `http://localhost:3000`.

---

## Usage

### Emotion Detection
1. Navigate to the frontend application.
2. Upload a photo of yourself using the "Upload Image" button.
3. The app will detect your emotion and display it on the screen.

### Diary Reflections
1. Write a daily reflection in the "Diary" section.
2. Submit the diary to analyze your mood.

### Generate Playlist
1. Click the "Generate Playlist" button.
2. The app will combine your detected emotion and diary mood to fetch a personalized playlist from Beatoven.ai.
3. Enjoy interactive visualizations of the playlist using D3.js and Three.js.

---

## Features in Detail

### Facial Expression Recognition
- **Library**: OpenCV
- **Model**: TensorFlow/Keras pre-trained emotion detection model
- **Input**: User-uploaded photo
- **Output**: Detected emotion (e.g., Happy, Sad, Neutral)

### Diary Sentiment Analysis
- **Library**: NLTK (SentimentIntensityAnalyzer)
- **Input**: Text from the user’s diary entry
- **Output**: Sentiment classification (e.g., Positive, Neutral, Negative)

### Beatoven.ai Integration
- **API**: Fetches playlists based on mood parameters.
- **Mood Mapping**:
  - Happy -> Energetic
  - Sad -> Calm
  - Neutral -> Balanced

### Visualizations
- **D3.js**: Displays a 2D scatterplot of songs with interactive tooltips.
- **Three.js**: Creates a 3D music sphere visualization.

---

## Deployment

### Backend Deployment
1. Install a production-ready WSGI server like `gunicorn`:
   ```bash
   pip install gunicorn
   ```
2. Deploy the backend to a cloud platform (e.g., AWS, Google Cloud, or Heroku).

### Frontend Deployment
1. Build the production-ready frontend:
   ```bash
   npm run build
   ```
2. Deploy it on platforms like **Netlify**, **Vercel**, or **AWS S3**.

---

## Future Extensions

1. **Smartwatch Integration**:
   - Use heart rate and other physiological data to refine emotion detection.
   - Combine with facial expressions and diary entries for improved personalization.

2. **User Profiles**:
   - Allow users to save and revisit their playlists and diary reflections.

3. **Real-Time Emotion Detection**:
   - Integrate webcam-based real-time emotion detection for continuous updates.

---

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
If you have any questions, feel free to contact me through Github.

