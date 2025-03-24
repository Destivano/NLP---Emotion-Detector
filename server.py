"""
Hello
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """
    Retrieve the text to analyze from the request arguments
    """
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid input! Try again."

    # Formatting the response
    formatted_response = ", ".join([f"'{k}': {v}" \
                        for k, v in response.items() \
                        if k != "dominant_emotion"])
    formatted_string = f"For the given statement,\
     the system response is {formatted_response}.\
      The dominant emotion is {response['dominant_emotion']}."
    return formatted_string

@app.route("/")
def render_index_page():
    """
    rendering the home page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
