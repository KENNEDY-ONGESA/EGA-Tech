# 🎨 Frontend Architecture: Vue.js

## 1. Overview

The frontend is built using **Vue.js 3** (Composition API) and styled with raw **CSS** for a custom, premium look. It serves as the interface where users select genres and view the generated playlists. We use **Vue CLI (Webpack)** for bundling the application.

## 2. Core Concepts

The entire logic is encapsulated in a single smart component: `PlaylistGenerator.vue`.

### A. The Logic (`<script setup>`)

We use Vue 3's **Composition API** for cleaner, more readable code.

- **Reactive State (`ref`):**

  - `selectedGenre`: Tracks what the user picked.
  - `playlist`: Stores the list of songs returned from the backend.
  - `loading`: A boolean flag to show/hide the "Loading..." spinner.

- **The `generatePlaylist` Function:**
  1.  **Input Validation:** Checks if a genre is actually selected.
  2.  **State Reset:** Clears previous results and sets `loading = true`.
  3.  **API Call:** Uses the native `fetch` API to POST data to `/api/generate-playlist`.
  4.  **Error Handling:** A `try/catch/finally` block ensures the UI doesn't freeze if the server fails.

### B. The User Interface (`<template>`)

The HTML structure is semantic and accessible.

- **Input Section:** A dropdown (`<select>`) bound to `selectedGenre` using `v-model`. This builds a two-way data binding.
- **Action Button:** The button is dynamically disabled (`:disabled`) if no genre is selected or if the app is currently loading.
- **Results Display:** We use `v-for` to loop through the `playlist` array and render each song. We also use `v-if="playlist.length > 0"` to hide the results section when it's empty.

### C. Styling (`<style scoped>`)

We use **Scoped CSS** to ensure styles don't leak to other parts of the app.

- **Theme:** A dark, cinematic theme using deep blacks (`#121212`) and bright accents (`#6366f1`).
- **Layout:** Heavily utilizes **Flexbox** for centering elements and handling responsiveness.
- **Polish:** Includes hover effects on buttons and subtle borders for a polished "glassy" feel.

## 3. Key Takeaway for Presentation

"The frontend is designed to be **stateless** and **resilient**. It doesn't matter how complex the backend AI logic is; the frontend simply requests data and displays it, handling loading states and errors gracefully to ensure a smooth user experience."
