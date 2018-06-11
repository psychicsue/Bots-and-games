from flask import Flask, request, config
from pymessenger.bot import Bot
from bot import bot_text_agent, respond_to

app = Flask(__name__)
ACCESS_TOKEN = ''
VERIFY_TOKEN = ''
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

                        text = message['message'].get('text')
                        response = bot_text_agent(text)

                        send_message(recipient_id, response)
                    else:
                        send_failure_message(recipient_id)

        return "Message Processed"

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

def send_failure_message(recipient_id):
    bot.send_text_message(recipient_id, respond_to("CANT_UNDERSTAND"))
    return "success"

def send_welcome_message(recipient_id):
    bot.send_text_message(recipient_id, respond_to("FACEBOOK_WELCOME"))
    return "success"

if __name__ == "__main__":
    app.run()