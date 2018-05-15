from slackclient import SlackClient

SLACK_TOKEN = "xoxb-346353260501-lrRidik99JvpYTyrjZDS9egw"

class ReactionEvent:
    def __init__(self):
        self.slack_client = SlackClient(SLACK_TOKEN)

    def get_users_by_email(self):
        listOfUsers = ""
        api_call = self.slack_client.api_call("users.lookupByEmail")
        if api_call.get('ok'):
            users = api_call.get('user')
            for user in users:
                listOfUsers += "<@" +  user.get('real_name') + "> \n"
        return listOfUsers

    def get_users(self):
        listOfUsers = ""
        profile = ""
        api_call = self.slack_client.api_call("users.list")
        if api_call.get('ok'):
            users = api_call.get('members')
            for user in users:
                listOfUsers += "<@" +  user.get('profile').get('display_name') + "> \n"
            return listOfUsers

    def get_user_conversations(self, user):
        listOfConversations = ""
        api_call = self.slack_client.api_call("conversations.user")
        if api_call.get('ok'):
            conversations = api_call.get('channels')
            for conv in conversations:
                listOfConversations += conv.get('name') + "\n"
        return listOfConversations

    def get_channels(self):
        listOfChannels = ""
        api_call = self.slack_client.api_call("channels.list")
        if api_call.get('ok'):
            channels = api_call.get('channels')
            for channel in channels:
                listOfChannels += channel.get('name') + "\n"
        return listOfChannels