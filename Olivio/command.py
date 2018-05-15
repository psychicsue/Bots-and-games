import random

import reaction_event


class Command(object):
    def __init__(self):
        self.reaction = reaction_event.ReactionEvent()
        self.commands = {
            "hi": self.hello,
            "help": self.help,
            "quote": self.quote,
        }
        self.bot_command = {
            "users": self.reaction.get_users(),
            "channels": self.reaction.get_channels(),
            "@": self.reaction.get_users_by_email()
        }

    def handle_command(self, user, command):
        response = "<@" + user + ">: "

        if command not in (self.commands or self.bot_command):
            response += "Sorry I don't understand the command: " + command + ". " + self.help()

        if command in self.commands:
            response += self.commands[command]()
        if command in self.bot_command:
            response = self.bot_command[command]

        return response

    def reaction(self, command):
        list = self.bot_command[command]()
        response = "".join(list)
        return response

    def quote(self):
        text_file = open("quotes.txt")
        list = text_file.readlines()
        return random.choice(list)

    def hello(self):
        list = ['Hi', 'How Are You?', 'Hello', 'Good morning', 'Have a nice day!']
        return random.choice(list)

    def help(self):
        response = "Currently I support the following commands:\r\n"

        for command in self.commands:
            response += command + "\r\n"

        for command in self.bot_command:
            response += command + "\r\n"

        return response