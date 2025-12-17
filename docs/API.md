# How to Test the API with Postman

One of your requirements is to demonstrate the API using Postman. Here is the step-by-step guide.

## 1. Setup

1.  Ensure your app is running (`start.bat`).
2.  Open **Postman** (or any API Client like Insomnia/Thunder Client).
3.  Create a **New Collection** named "Music Generator".

## 2. Testing the Health Check

- **Method**: `GET`
- **URL**: `http://127.0.0.1:5000/health`
- **Send Request**.
- **Expected Result**:
  ```json
  {
    "status": "ok"
  }
  ```
  _Screenshot this for your report._

## 3. Testing Playlist Generation (The Main Feature)

- **Method**: `POST` (Change GET to POST in the dropdown).
- **URL**: `http://127.0.0.1:5000/generate-playlist`
- **Body Tab**:
  1.  Click the **"Body"** tab below the URL bar.
  2.  Select **"raw"**.
  3.  In the dropdown that says "Text", change it to **"JSON"**.
  4.  Paste this JSON payload:
      ```json
      {
        "genre": "Rock"
      }
      ```
- **Send Request**.

### Expected Response

You should see a status `200 OK` and a response body like:

```json
{
    "playlist": [
        {
            "title": "Bohemian Rhapsody",
            "artist": "Queen"
        },
        {
            "title": "Stairway to Heaven",
            "artist": "Led Zeppelin"
        },
        ...
    ],
    "source": "ai"
}
```

## 4. Testing Error Handling (Bonus Points)

To prove your code is robust, test a failure case.

1.  **Empty Request**:
    - Send the same request but with an empty body `{}`.
    - **Expected Result**: Status `400 Bad Request` and message `{"error": "Genre is required"}`.

## Why use Postman?

The frontend is just one way to access your backend. Postman proves that your backend is a standalone Service that _anyone_ (Mobile App, Desktop App, another Website) could use. This is the definition of a powerful API.
