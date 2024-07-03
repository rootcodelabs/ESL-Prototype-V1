import React, { useState } from "react";
import axios from "axios";
import RingLoader from "react-spinners/RingLoader";
import "./App.css";

function App() {
  const [phrase, setPhrase] = useState("");
  const [videoUrl, setVideoUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setVideoUrl("");

    try {
      const response = await axios.post(
        "http://localhost:8000/api/generate_video",
        { phrase },
        {
          responseType: "blob",
          headers: {
            "Content-Type": "application/json",
            Accept: "video/mp4",
          },
        }
      );

      const videoBlob = new Blob([response.data], { type: "video/mp4" });
      const url = URL.createObjectURL(videoBlob);
      setVideoUrl(url);
    } catch (error) {
      console.error("Error generating video:", error);
      setError(
        "An error occurred while generating the video. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="content">
        <h1>Estonian Sign Language Video Generator</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={phrase}
            onChange={(e) => setPhrase(e.target.value)}
            placeholder="Enter a phrase"
            required
          />
          <button type="submit" disabled={loading}>
            {loading ? "Generating..." : "Generate Video"}
          </button>
        </form>
        {loading && (
          <div className="loader">
            <RingLoader color="#2a55e5" size={120} />
          </div>
        )}
        {error && <p className="error">{error}</p>}
        {videoUrl && (
          <div>
            <h2>Generated Video:</h2>
            <video src={videoUrl} controls width="640" height="480" />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
