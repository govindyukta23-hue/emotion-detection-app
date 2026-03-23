import requests

def emotion_detector(text_to_analyze):
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID/v1/analyze?version=2021-08-01"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "text": text_to_analyze,
        "features": {
            "emotion": {}
        }
    }

    response = requests.post(
        url,
        json=data,
        headers=headers,
        auth=("apikey", "YOUR_API_KEY")
    )

    if response.status_code == 200:
        emotions = response.json()["emotion"]["document"]["emotion"]

        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion
        }

    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }


print(emotion_detector("I am very happy today!"))
