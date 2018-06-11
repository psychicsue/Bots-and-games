import string
from weather import Weather
from nlp.Detection import get_chunks
from imgur import get_meme

def bot_text_agent(text):

    if small_talk_detection(text) is not None:
        idx = small_talk_detection(text)
        return small_talk_answer(idx)

    elif GPE_detection(text):
        city = get_chunks(text, 'GPE')[0]
        print('GPE DETECTED')
        return weather_agent(city)

    else:
        return respond_to("CANT_UNDERSTAND") + "\n" + get_meme()


def GPE_detection(text):
    return True if len(get_chunks(text, 'GPE')) > 0 else False

def weather_agent(city=None, cord=None):
    try:
        if city is not None:
            weather = Weather(city)
            return retrieve_responses(weather, city)
        elif cord is not None:
            weather = Weather(cord=cord)
            return retrieve_responses(weather)
    except Exception:
        response = respond_to("NOT_FOUND") + "\n" +get_meme()
        return response


def respond_to(key=None):
    respond = {
        "FACEBOOK_WELCOME": 'Hi there !, I am Oliv and I can check the weather for you',
        "NOT_FOUND": "Sorry, My mom didn't teach me about this city !",
        "GET_STARTED": "How would you like to get a weather forecast?",
        "CANT_UNDERSTAND": "I can't understand your sentence !",
        "DEFAULT": "Give me time, I'm still learning!"
    }
    return respond[key] if key is not None else respond["DEFAULT"]

def small_talk():
    return [
        {
            'QUESTION': "Are you there?",
            'ANSWER': "I am Here to find the weather forecast. Tell me your city name"
        },
        {
            'QUESTION': "How old are you?",
            'ANSWER': "Older than you might think, but young enough to talk with you"
        },
        {
            'QUESTION': "You are beautiful",
            'ANSWER': "I know, but thanks"
        },
        {
            'QUESTION': "You are a chatbot",
            'ANSWER': "Maybe, there is no proof, Ask me about the weather via location or city name and i will be glad to find it"
        },
        {
            'QUESTION': "Are you ready?",
            'ANSWER': "Yes, Just give me your location or city name"
        },
        {
            'QUESTION': "You're so clever.",
            'ANSWER': "I was created by clever women"
        },
        {
            'QUESTION': "How Are you?",
            'ANSWER': "I'm new born :) How are you?"
        },
        {
            'QUESTION': "Good",
            'ANSWER': "Ask me about the weather via location or city name and i will be glad to find it"
        },
        {
            'QUESTION': "Hello",
            'ANSWER': "Hi there !, I am Oli and I can check the weather for you. Please ask me about weather for the city ;) "
        },
        {
            'QUESTION': "Ping",
            'ANSWER': "Pong"
        }
    ]


def small_talk_detection(text):
    talks = small_talk()
    text = remove_punctuation(text)
    for idx, talk in enumerate(talks):
        if text.lower() in talk['QUESTION'].lower():
            return idx


def small_talk_answer(idx):
    return small_talk()[idx]['ANSWER']


def retrieve_responses(weather_provider, city):
    temp = str(weather_provider.get_temp())
    humidity = str(weather_provider.get_humidity())
    wind = str(weather_provider.get_wind_speed())
    max_temp = str(weather_provider.get_max_temp())
    min_temp = str(weather_provider.get_min_temp())
    status = str(weather_provider.get_status())

    # string type
    response = " Today's forecast for " + city +  \
               "\n Temperature is " + temp + " Celsius " \
               "\n Max. temperature is " + max_temp + " Celsius " \
               "\n Min. temperature is " + min_temp + " Celsius " \
               "\n Humidity is " + humidity + " % " \
               "\n Weather status " + status + \
               "\n Wind speed is " + wind + " m/s"

    return response


def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))