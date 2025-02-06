from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    textToanalyze = request.args.get('textToAnalyze')
    respdd = emotion_detector(textToanalyze)
    angerscore = respdd['anger']
    disgustscore = respdd['disgust']
    fearscore = respdd['fear']
    joyscore = respdd['joy']
    sadnessscore = respdd['sadness']
    domemotion = respdd['dominant_emotion']
    response = ""
    if domemotion != None:
        response = f"For the statement: '{textToanalyze}' the system response is "
        response += f"'anger':{angerscore}, "
        response += f"'disgust':{disgustscore}, "
        response += f"'fear':{fearscore}, "
        response += f"'joy':{joyscore}, "
        response += f"'sadness':{sadnessscore}. "
        response += f"The dominant emotion is {domemotion}."
    else:
        response = "Invalid text! Please try again!"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)