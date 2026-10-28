# Final Project

A Python Flask application that detects anger, disgust, fear, joy, and sadness using the Watson NLP emotion endpoint.

## Files

- `EmotionDetection/emotion_detection.py`: emotion detection function and output formatting.
- `EmotionDetection/__init__.py`: package initializer.
- `test_emotion_detection.py`: unit tests.
- `server.py`: Flask web application.
- `templates/index.html`: browser interface.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate with `.venv\Scripts\activate`.

## Test

```bash
python -m unittest -v
```

The tests mock the remote service so they can test output formatting and error handling without relying on network availability.

## Run the web app

```bash
python server.py
```

Open `http://127.0.0.1:5000`.

## Static analysis

```bash
pylint server.py
```
