import command

class Event:
    def __init__(self, bot):
        self.bot = bot
        self.command = command.Command()

    def wait_for_event(self):
        events = self.bot.slack_client.rtm_read()

        if events and len(events) > 0:
            for event in events:
                print(event)
                self.parse_event(event)

    def parse_event(self, event):
        if "message" in event['type'] and 'text' in event and self.bot.name in event['text']:
            self.handle_event(event['user'], event['text'].split(self.bot.name)[1].strip().lower(), event['channel'])
        if 'team_join' in event['type']:
            response = "Welcome on board" + event['user']
            self.bot.slack_client.api_call("chat.postMessage", channel = event['channel'], text=response, as_user=True)
        if 'reaction_added' in event['type']:
            self.handle_reaction_event(event['item'], event['reaction'], event['event_ts'])

    def get_emoji_list(self):
        api_call = self.bot.slack_client.api_call("emoji.list")
        if api_call.get('ok'):
            return api_call.get('emoji')

    def handle_event(self, user, command, channel):
        if command and channel:
            "Received command: " + command + " in channel: " + channel + " from user: " + user
            response = self.command.handle_command(user, command)
            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

    def handle_reaction_event(self, item, emoji, timestamp):
        channel = item['channel']
        print(channel)
        print(self.bot.slack_client.api_call("reactions.remove",channel = channel, name = emoji, timestamp = timestamp, as_user = True))

    def filter_files(self, timestamp):
        api_call = self.bot.slack_client.api_call("files.list")
        files = api_call.get('files')
        for file in files:
            print(file)