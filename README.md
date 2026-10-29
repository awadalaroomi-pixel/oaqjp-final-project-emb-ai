# Emotion Detection using Watson NLP

## Project Overview

This project is a Flask-based web application that detects emotions in text using the Watson Natural Language Processing (NLP) Emotion Detection service.

The application identifies five emotions:
- Anger
- Disgust
- Fear
- Joy
- Sadness

## Technologies Used

- Python
- Flask
- Watson NLP Emotion Detection API
- Requests
- Unit Testing with nose
- GitHub Actions
- OpenShift Pipelines and Tekton

## Features

- Analyze text and identify its emotions.
- Return emotion scores and the dominant emotion.
- Provide a simple interface for emotion detection.
- Support automated linting and unit testing.

## Installation

1. Clone the repository.
2. Install the dependencies:

   pip install -r requirements.txt

3. Run the Flask application:

   python server.py

## Testing

Run the unit tests using the test configuration provided in the project.

## Continuous Integration

The GitHub Actions workflow is located at:
.github/workflows/workflow.yml

The Tekton task definitions are located at:
.tekton/tasks.yml

## Project Repository

https://github.com/awadalaroomi-pixel/oaqjp-final-project-emb-ai
