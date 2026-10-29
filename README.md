# Emotion Detection using Watson NLP

## Project Overview

This project implements an emotion detection application using Python, Flask, and the Watson Natural Language Processing (NLP) Emotion Detection service.

The application analyzes a text input and identifies the emotions expressed in it.

The five emotions detected are:
- Anger
- Disgust
- Fear
- Joy
- Sadness

## Project Objectives

- Detect emotions in text using Watson NLP.
- Identify the dominant emotion in a text input.
- Provide an application interface for emotion analysis.
- Apply software testing and continuous integration practices.

## Technologies Used

- Python
- Flask
- Watson NLP Emotion Detection
- Requests
- Nose for unit testing
- Flake8 for code linting
- GitHub Actions for continuous integration
- OpenShift Pipelines and Tekton

## Project Structure

```text
oaqjp-final-project-emb-ai/
├── .github/
│   └── workflows/
│       └── workflow.yml
├── .tekton/
│   └── tasks.yml
├── EmotionDetection/
├── README.md
├── requirements.txt
├── server.py
└── test_emotion_detection.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/awadalaroomi-pixel/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python server.py
```

## Testing

The project includes a unit test file named `test_emotion_detection.py`.

Install the project dependencies before running the tests.

To execute the unit tests with nose, use:

```bash
nosetests -v
```

The tests should be reviewed to ensure the emotion detection functionality works as expected.

## Code Quality

Flake8 can be used to check Python code for style and syntax issues:

```bash
flake8 .
```

## Continuous Integration

The GitHub Actions workflow configuration is located at:

`.github/workflows/workflow.yml`

The workflow is intended to automate dependency installation, code linting, unit testing, and application build checks.

## OpenShift and Tekton

The Tekton task definitions are located at:

`.tekton/tasks.yml`

The pipeline tasks for the CI/CD process include:

1. `cleanup`
2. `git-clone`
3. `flake8`
4. `nose`
5. `buildah`
6. `openshift-client`

These tasks represent the intended stages of the pipeline. Their actual execution depends on the pipeline configuration and OpenShift environment.

## Repository

Public GitHub repository:

https://github.com/awadalaroomi-pixel/oaqjp-final-project-emb-ai

## License

This project is intended for educational purposes.
