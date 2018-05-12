import command
import command_reaction


class Event:
    def __init__(self, bot):
        self.bot = bot
        self.command = command.Command()
        self.command_reaction = command_reaction.CommandReaction()

    def wait_for_event(self):
        events = self.bot.slack_client.rtm_read()

        if events and len(events) > 0:
            for event in events:
                print(event)
                self.parse_event(event)

    def parse_event(self, event):
        if "message" in event['type'] and 'text' in event and self.bot.name in event['text']:
            self.handle_event(event['user'], event['text'].split(self.bot.name)[1].strip().lower(), event['channel'])
        elif "message" in event['type']:
            self.handle_reaction_event(event['user'], event['text'], event['channel'])
        if 'team_join' in event['type']:
            response = "Welcome on board" + event['user']
            self.bot.slack_client.api_call("chat.postMessage", channel = event['channel'], text=response, as_user=True)
        # if 'reaction_added' in event['type']:
        #     self.bot.slack_client.api_call("reactions.add", channel = event['channel'], name)

    def handle_reaction_event(self, user, command, channel):
        if command and channel:
            response = self.command_reaction.handle_reaction_command(command)
            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

    def handle_event(self, user, command, channel):
        if command and channel:
            print("Received command: " + command + " in channel: " + channel + " from user: " + user)
            print(user)
            response = self.command.handle_command(user, command)
            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

    def get_users_by_email(self, event):
        api_call = self.bot.slack_client.api_call("users.lookupByEmail")
        if api_call.get('ok'):
            users = api_call.get('users')
            for user in users:
                return user.get('real_name')