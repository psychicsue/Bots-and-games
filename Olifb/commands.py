import random

class Command(object):
    def __init__(self):
        self.commands = {
            "hi": self.hello,
            "help": self.help,
            "quote": self.quote,
        }

    def handle_command(self, user, command):
        response = ""

        if command not in (self.commands):
            response += "Sorry I don't understand the command: " + command + ". " + self.help()

        if command in self.commands:
            response += self.commands[command]()

        return response

    def reaction(self, command):
        list = self.bot_command[command]()
        response = "".join(list)
        return response

    def help(self):
        response = "Currently I support the following commands:\r\n"

        for command in self.commands:
            response += command + "\r\n"

        for command in self.bot_command:
            response += command + "\r\n"

        return response