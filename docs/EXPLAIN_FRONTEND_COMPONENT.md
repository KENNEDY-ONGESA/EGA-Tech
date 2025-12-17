# Deep Dive: `frontend/src/components/PlaylistGenerator.vue`

This is a **Single File Component (SFC)** in Vue.js. It encapsulates the HTML (Template), Logic (Script), and Styling (CSS) for the main feature of the app.

## 1. The `<script setup>` Block

We are using **Vue 3 Composition API** (`<script setup>`), which is the modern standard. It is more concise than the older Options API.

### Imports

```javascript
import { ref } from "vue";
```

- **`ref`**: The essential building block of Reactivity. Any variable created with `ref()` will automatically trigger a UI update (re-render) whenever its value changes.

### State Variables (Reactive Data)

```javascript
const selectedGenre = ref("");
const playlist = ref([]);
const loading = ref(false);
```

- **`selectedGenre`**: Strings bind to the dropdown.
- **`playlist`**: Array that stores the song objects fetched from the API.
- **`loading`**: Boolean flag. formatting logic depends on this (e.g., showing a spinner vs "Generate" button).

### Function: `generatePlaylist`

This is an **Async Function** because network requests take time.

1.  **State Reset**: `loading.value = true; playlist.value = [];`
    - Immediate user feedback. Clears old data and starts the spinner.
2.  **Network Request**:
    ```javascript
    await fetch('/api/generate-playlist', ...)
    ```
    - It calls our own backend (proxy leads to localhost:5000).
    - **`JSON.stringify`**: Converts our Javascript object `{ genre: 'Pop' }` into a text string for transport.
3.  **Error Handling**:
    - Uses a `try/catch` block. If the backend is offline (Network Error), it catches it so the app doesn't crash white-screen.
4.  **Finally Block**: `loading.value = false;`
    - Runs whether the request succeeded OR failed. Ensures the button is re-enabled so the user isn't stuck typically spinning forever.

---

## 2. The `<template>` Block

This defines the structure (DOM) based on the state.

### Directive: `v-model`

```html
<select v-model="selectedGenre"></select>
```

- **Two-Way Binding**: If the user picks an option, `selectedGenre` updates. If code changes `selectedGenre`, the dropdown updates.

### Directive: `v-for`

```html
<option v-for="genre in genres" :key="genre"></option>
```

- **List Rendering**: Loops through the `genres` array to create `<option>` tags dynamically.

### Event Handling: `@click`

```html
<button @click="generatePlaylist" :disabled="..."></button>
```

- Listens for the click event.
- **:disabled**: Dynamic attribute. We disable the button if no genre is picked OR if we are currently loading.

### Conditional Rendering: `v-if`

```html
<div v-if="playlist.length > 0" ...></div>
```

- The results container doesn't exist in the DOM until we actually have results. This keeps the UI clean.

---

## 3. The `<style scoped>` Block

**`scoped`**: This is critical. It means these CSS rules apply **ONLY** to this component.

- Example: If we style `.title { color: red }` here, it won't accidentally turn titles red in other parts of the app.

### Key CSS Techniques Used:

- **Glassmorphism**:
  ```css
  background: rgba(40, 40, 40, 0.7);
  backdrop-filter: blur(20px);
  ```
  Creates the modern "frosted glass" look by blurring whatever is behind the element.
- **Transitions & Animations**:
  - `.song-item` has `animation: slideIn ...`.
  - We use simple CSS keyframes to make items slide up and fade in nicely when they appear.
