from imgurpython import ImgurClient
import random

ImgurClientID = 'bec32a13abf65e1'
ImgurClientSecret = '0ebab2bb3d2a391907c2718dc74bb80c78da93ff'

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