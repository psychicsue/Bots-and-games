from imgurpython import ImgurClient
import random

ImgurClientID = ''
ImgurClientSecret = ''

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