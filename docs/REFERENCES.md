# External References & Resources

Here is a list of trusted resources and tutorials that can be cited to explain the "Advanced" parts of the codebase.

## 1. CSS Glassmorphism

- **Concept**: Creating a frosted-glass effect using `backdrop-filter`.
- **Source**: [CSS Glassmorphism Generator](https://glassmorphism.com/)
  - _Usage_: Used to generate the `background`, `backdrop-filter`, and `border` properties for the `.generator-card` class in `PlaylistGenerator.vue`.
- **Tutorial**: [CSS-Tricks: Glassmorphism](https://css-tricks.com/glassmorphism-css-generator/)
  - _Key properties learned_: `backdrop-filter: blur(20px)`, `background: rgba(...)`.

## 2. Text Gradient

- **Concept**: Making text look like it has a gradient color.
- **Source**: [W3Schools: CSS Text Gradient](https://www.w3schools.com/howto/howto_css_text_gradient.asp)
  - _Usage_: Used for the "Vibe Curator" title.
  - _Key Code_: `-webkit-background-clip: text; color: transparent;`

## 3. Bash Scripting (Parallel Execution)

- **Concept**: Running two programs (Backend & Frontend) in the same terminal window.
- **Source**: [StackOverflow: How to run two commands in parallel?](https://stackoverflow.com/questions/3004811/how-do-you-run-multiple-programs-in-parallel-from-a-bash-script)
  - _Key learning_: Using the `&` symbol to run in background and `wait` to keep the script alive.
  - _Snippet_: `python app.py & npm run dev & wait`

## 4. Python JSON Extraction (Regex)

- **Concept**: Extracting a JSON block from a larger string of AI chatter.
- **Source**: [StackOverflow: Extract info inside a json string using python regex](https://stackoverflow.com/questions/59074765/extract-info-inside-a-json-string-using-python-regex)
  - _Usage_: The logic in `app.py` to find `[` and `]` brackets.
  - _Pattern_: `re.search(r'\[.*\]', text, re.DOTALL)`

## 5. Vite Proxy Configuration

- **Concept**: Forwarding `/api` requests to a different backend port to avoid CORS.
- **Source**: [Vite Documentation: Server Proxy](https://vitejs.dev/config/server-options.html#server-proxy)
  - _Usage_: The `server: { proxy: { ... } }` block in `vite.config.js`.
  - _Key settings_: `changeOrigin: true` and `rewrite`.
