import requests, json

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    request_obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = request_obj, headers=header)  
    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Create a new dictionary to hold emotions,
    # the 'dominant_emotion' will be appended later
    # after finding out which value in the dictionary 
    # has the highest value
    output_emotions = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }

    max_emotion_value = max(output_emotions.values())

    for k, v in output_emotions.items():
        if v == max_emotion_value:
            max_emotion_name = k
            break
    
    # Append the 'dominant_emotion' to the dictionary
    output_emotions['dominant_emotion'] = max_emotion_name
    return output_emotions


