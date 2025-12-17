# Deep Dive: `vite.config.js`

This file is the **control center** for your frontend build tool (Vite). It tells Vite how to behave when you are developing locally.

## 1. Imports

```javascript
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
```

- **`defineConfig`**: A helper function that gives you auto-completion (IntelliSense) in your editor.
- **`vue`**: The plugin that teaches Vite how to read `.vue` files. Without this, standard JavaScript tools wouldn't understand your Single File Components.

## 2. Configuration Object

### `plugins: [vue()]`

- This activates the Vue plugin we imported. It compiles your `<template>`, `<script>`, and `<style>` blocks into raw JavaScript and CSS that the browser can understand.

### `server.proxy` (The Critical Part)

This section solves the **Cross-Origin (CORS)** problem during development.

```javascript
server: {
  proxy: {
    '/api': {
      target: 'http://127.0.0.1:5000',
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/api/, '')
    }
  }
}
```

- **The Problem**: Your frontend runs on port **5173**. Your backend runs on port **5000**. Browsers consider these different "Worlds" (Origins) and mostly block them from talking to avoid security risks.
- **The Solution**: We create a fake "middleman" (Proxy) in Vite.

**How it works step-by-step:**

1.  Frontend code asks for: `http://localhost:5173/api/generate-playlist`
    - _(Note: It asks its own server, port 5173, not 5000)_.
2.  Vite sees the prefix **`/api`**.
3.  Vite says: "Aha! I have a rule for this."
4.  **`target`**: It forwards the request secretly to `http://127.0.0.1:5000`.
5.  **`rewrite`**: It strips away the `/api` prefix.
    - Incoming: `/api/generate-playlist`
    - Outgoing to Backend: `/generate-playlist`
    - _Why?_ Because your Flask app defines `@app.route('/generate-playlist')`, not `/api/generate-playlist`. The `/api` prefix is just a label for the frontend to know "this is for the backend".
6.  **`changeOrigin: true`**: It tricks the backend into thinking the request came from port 5000 (itself), preventing weird host header issues.

## Summary for Presentation

"This file bridges the gap between our Frontend and Backend. It sets up a development proxy so the frontend doesn't need to know the backend's exact address, and it uses the Vue plugin to compile our code."
