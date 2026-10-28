"""Unit tests for the emotion detection module."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import EMOTION_URL, emotion_detector


def make_response(scores, status_code=200):
    """Create a mock Watson response containing the supplied emotion scores."""
    response = Mock()
    response.status_code = status_code
    response.raise_for_status.return_value = None
    response.json.return_value = {
        "emotionPredictions": [{"emotion": scores}]
    }
    return response


class TestEmotionDetector(unittest.TestCase):
    """Tests for emotion_detector output and error handling."""

    def test_joy_is_dominant(self):
        scores = {
            "anger": 0.01, "disgust": 0.01, "fear": 0.02,
            "joy": 0.94, "sadness": 0.02,
        }
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=make_response(scores),
        ) as post:
            result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")
        post.assert_called_once()
        self.assertEqual(post.call_args.args[0], EMOTION_URL)

    def test_anger_is_dominant(self):
        scores = {
            "anger": 0.90, "disgust": 0.02, "fear": 0.02,
            "joy": 0.03, "sadness": 0.03,
        }
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=make_response(scores),
        ):
            result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust_is_dominant(self):
        scores = {
            "anger": 0.02, "disgust": 0.91, "fear": 0.02,
            "joy": 0.02, "sadness": 0.03,
        }
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=make_response(scores),
        ):
            result = emotion_detector("I feel disgusted")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness_is_dominant(self):
        scores = {
            "anger": 0.02, "disgust": 0.02, "fear": 0.03,
            "joy": 0.03, "sadness": 0.90,
        }
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=make_response(scores),
        ):
            result = emotion_detector("I am so sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear_is_dominant(self):
        scores = {
            "anger": 0.02, "disgust": 0.02, "fear": 0.90,
            "joy": 0.03, "sadness": 0.03,
        }
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=make_response(scores),
        ):
            result = emotion_detector("I am afraid")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_blank_input_returns_empty_result(self):
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["joy"])

    def test_http_400_returns_empty_result(self):
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=make_response({}, status_code=400),
        ):
            result = emotion_detector("invalid")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
