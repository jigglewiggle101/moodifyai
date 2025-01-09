import React, { useState } from "react";
import Diary from "./Diary";
import PlaylistVisualization from "./PlaylistVisualization";
import axios from "axios";

const App = () => {
  const [emotion, setEmotion] = useState("");
  const [diaryMood, setDiaryMood] = useState("");
  const [playlist, setPlaylist] = useState([]);

  const handleImageUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("image", file);

    try {
      const response = await axios.post("http://localhost:5000/detect-emotion", formData);
      setEmotion(response.data.emotion);
    } catch (error) {
      console.error("Error detecting emotion:", error);
    }
  };

  const handleDiarySubmit = async (diaryText) => {
    try {
      const response = await axios.post("http://localhost:5000/analyze-diary", { text: diaryText });
      setDiaryMood(response.data.mood);
    } catch (error) {
      console.error("Error analyzing diary:", error);
    }
  };

  const fetchPlaylist = async () => {
    try {
      const response = await axios.post("http://localhost:5000/get-playlist", { emotion, diaryMood });
      setPlaylist(response.data.songs || []);
    } catch (error) {
      console.error("Error fetching playlist:", error);
    }
  };

  return (
    <div>
      <h1>Emotion & Diary-Based Music Playlist</h1>
      <input type="file" accept="image/*" onChange={handleImageUpload} />
      <Diary onSubmit={handleDiarySubmit} />
      <button onClick={fetchPlaylist}>Generate Playlist</button>
      <PlaylistVisualization playlist={playlist} />
    </div>
  );
};

export default App;
