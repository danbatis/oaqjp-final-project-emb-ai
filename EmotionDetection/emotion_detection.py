import requests
import json

def emotion_detector(text_to_analyse):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    injson={ "raw_document": { "text": text_to_analyse } }
    #send it to the Watson API
    rawresp = requests.post(url, json = injson, headers=headers)
    
    anger_score = None
    disgust_score = None
    fear_score = None
    joy_score = None
    sadness_score = None
    #finding the highest score
    dominant_emotion = None

    if rawresp.status_code == 200:
        #convert to dict
        respdd = json.loads(rawresp.text)
        #formatting it
        emodd = respdd['emotionPredictions'][0]['emotion']
        anger_score = emodd['anger']
        disgust_score = emodd['disgust']
        fear_score = emodd['fear']
        joy_score = emodd['joy']
        sadness_score = emodd['sadness']
        #finding the highest score
        dominant_emotion = 'anger'
        domscore = anger_score
        if disgust_score > domscore:
            dominant_emotion = 'disgust'
            domscore=disgust_score
        if fear_score> domscore:
            dominant_emotion = 'fear'
            domscore = fear_score
        if joy_score > domscore:
            dominant_emotion = 'joy'
            domscore = joy_score
        if sadness_score > domscore:
            dominant_emotion = 'sadness'
            domscore = sadness_score
    if rawresp.status_code == 500:
        dominant_emotion = "Watson not able to process the statement!"
    return {'anger': anger_score,'disgust': disgust_score,
            'fear':fear_score,
            'joy':joy_score,
            'sadness':sadness_score,
            'dominant_emotion':dominant_emotion}