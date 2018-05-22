import time
import event
from slackclient import SlackClient

SLACK_TOKEN = ""

class Bot(object):
    def __init__(self):
        self.slack_client = SlackClient(SLACK_TOKEN)
        self.name = "oli"
        self.id = self.get_bot_id()
        self.emoji = ":robot_face:"

        if self.id is None:
            exit("Error, could not find bot" + self.name)
        print(id)

        self.event = event.Event(self)
        self.listen()

    def listen(self):
        if self.slack_client.rtm_connect(with_team_state=False):
            print("Olivio connected")
        while True:
            self.event.wait_for_event()

            time.sleep(1)
        else:
            exit("Connection failed")

    def get_bot_id(self):
        api_call = self.slack_client.api_call("users.list")
        if api_call.get('ok'):
            users = api_call.get('members')
            for user in users:
                print(user)
                if 'name' in user and user.get('name') == self.name:
                    return "<@" + user.get('id') + ">"
            return None

    def set_bot_emoji(self):
        api_call = self.slack_client.api_call("users.list")
        if api_call.get('ok'):
            users = api_call.get('members')
            for user in users:
                print(user)
                if 'name' in user and user.get('name') == self.name:
                    return "<@" + user.get('id') + ">"
            return None