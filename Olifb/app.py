from flask import Flask, request, config
from pymessenger.bot import Bot
from imgurpython import ImgurClient
import random

app = Flask(__name__)
ACCESS_TOKEN = ''
VERIFY_TOKEN = ''
ImgurClientID = ''
ImgurClientSecret = ''
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
        return "Message Processed"

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def get_message():
    response = "Hi! Here is Oli, your friends and companion"
    return get_meme()

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

def firstEntity(nlp, name):
  return nlp and nlp.entities and nlp.entities[name] and nlp.entities[name][0]


def handleMessage(message) :
    greeting = firstEntity(message.nlp, 'greetings')
    if greeting and greeting.confidence > 0.8:
        bot.send_text_message('Hi there!')

def get_meme():
    try:
        client = ImgurClient(ImgurClientID, ImgurClientSecret)
    except BaseException as e:
        print('[EROR] Error while authenticating with Imgur:', str(e))
        return

    items = client.gallery()
    list = []
    for item in items:
        list.append(item.link)
    return random.choice(list)

if __name__ == "__main__":
    app.run()