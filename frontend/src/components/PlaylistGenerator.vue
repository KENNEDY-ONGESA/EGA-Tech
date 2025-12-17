<script setup>
import { ref } from 'vue'

const selectedGenre = ref('')
const playlist = ref([])
const loading = ref(false)
// 1. Define available genres
const genres = ['Pop', 'Jazz', 'Rock', 'Hip Hop', 'Classical', 'Electronic', 'R&B', 'Country','Ohangla']

// 2. Main function to handle playlist generation
const generatePlaylist = async () => {
  if (!selectedGenre.value) return;
  
  // 3. Set loading state and reset current playlist
  loading.value = true;
  playlist.value = [];
  
  try {
    // 4. Send request to Backend (Use env var for Prod, or proxy for Dev)
    const apiUrl = process.env.VUE_APP_API_URL 
      ? `${process.env.VUE_APP_API_URL}/generate-playlist` 
      : '/api/generate-playlist';

    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ genre: selectedGenre.value }),
    });
    
    // 5. process the JSON response
    const data = await response.json();
    if (data.playlist) {
      playlist.value = data.playlist;
    } else {
      console.error("No playlist returned", data);
    }
  } catch (error) {
    // 6. Handle any network or API errors
    console.error("Error fetching playlist:", error);
  } finally {
    // 7. Turn off loading spinner
    loading.value = false;
  }
}
</script>

<template>
  <!-- 8. Main Container for the Application UI -->
  <div class="generator-container">
    <h1 class="title">🎵 Music Playlist Generator</h1>
    <h3 class="subtitle">Create a custom playlist based on your favorite genre.</h3>
    
    <!-- 9. Input Controls Section (Dropdown + Button) -->
    <div class="controls-row">
      <div class="input-group">
        <label for="genre-select" class="label-text">Select Genre:</label>
        <div class="select-wrapper">
          <!-- 10. Genre Selection Dropdown -->
          <select id="genre-select" v-model="selectedGenre" class="genre-select">
            <option disabled value="">Select</option>
            <option v-for="genre in genres" :key="genre" :value="genre">{{ genre }}</option>
          </select>
          <div class="select-arrow">▼</div>
        </div>
      </div>
      
      <!-- 11. Generate Button (Triggers API call) -->
      <button @click="generatePlaylist" :disabled="!selectedGenre || loading" class="generate-btn">
        <span v-if="loading">Loading...</span>
        <span v-else>Generate Playlist</span>
      </button>
    </div>

    <!-- 12. Results Section (Only visible when playlist has songs) -->
    <div v-if="playlist.length > 0" class="playlist-container">
      <h2>Your {{ selectedGenre }} Mix</h2>
      <ul class="playlist">
        <!-- 13. Song List Item (Iterates through songs) -->
        <li v-for="(song, index) in playlist" :key="index" class="song-item">
          <span class="song-number">{{ index + 1 }}</span>
          <div class="song-info">
            <span class="song-title">{{ song.title }}</span>
            <span class="song-artist">{{ song.artist }}</span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
/* 14. Container Layout & Aesthetics */
.generator-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 900px;
  margin: 0 auto;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 3rem;
}

/* 15. Typography Styles */
.title {
  font-size: 3rem;
  margin-bottom: 4rem;
  color: white;
  font-weight: 700;
}
.subtitle {
  font-size: 1rem;
  margin-bottom: 4rem;
  color: white;
  font-weight: 700;
}

/* 16. Input Controls Layout */
.controls-row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  width: 100%;
  max-width: 800px;
}

.input-group {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.label-text {
  font-size: 1.2rem;
  color: #cccccc;
}

.select-wrapper {
  position: relative;
  width: 200px;
}

/* 17. Form Elements Styling */
.genre-select {
  width: 100%;
  padding: 0.8rem 1rem;
  border-radius: 8px;
  background-color: #121212;
  border: 1px solid #333;
  color: white;
  font-size: 1rem;
  appearance: none;
  cursor: pointer;
}

.select-arrow {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
  font-size: 0.8rem;
  color: #aaa;
}

.generate-btn {
  padding: 0.8rem 2rem;
  border-radius: 8px;
  border: none;
  background-color: #6366f1; /* Indigo-ish color from image */
  color: white;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
}

.generate-btn:hover:not(:disabled) {
  background-color: #4f46e5;
}

.generate-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* 18. Playlist Results Styling */
.playlist-container {
  margin-top: 4rem;
  width: 100%;
  max-width: 600px;
  text-align: left;
}

.playlist-container h2 {
    color: #fff;
    margin-bottom: 1.5rem;
    text-align: center;
}

.playlist {
  list-style: none;
  padding: 0;
}

.song-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #333;
}

.song-number {
  color: #666;
  margin-right: 1.5rem;
  font-weight: bold;
}

.song-info {
  display: flex;
  flex-direction: column;
}

.song-title {
  color: white;
  font-weight: 500;
  font-size: 1.1rem;
}

.song-artist {
  color: #888;
  font-size: 0.9rem;
}
</style>
