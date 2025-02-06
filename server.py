'''
    server to run and analyze text using the Watson api
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    '''
    function to render the page
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    '''
    function to analyze and find emotions using the Watson api
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    respdd = emotion_detector(text_to_analyze)
    angerscore = respdd['anger']
    disgustscore = respdd['disgust']
    fearscore = respdd['fear']
    joyscore = respdd['joy']
    sadnessscore = respdd['sadness']
    domemotion = respdd['dominant_emotion']
    response = ""
    if domemotion is not None:
        response = f"For the statement: '{text_to_analyze}' the system response is "
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
