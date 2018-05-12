import random

class Command(object):
    def __init__(self):
        self.commands = {
            "hi": self.hello,
            "help": self.help,
            "quote": self.quote
        }

    def handle_command(self, user, command):
        response = "<@" + user + ">: "

        if command in self.commands:
            response += self.commands[command]()
        else:
            response += "Sorry I don't understand the command: " + command + ". " + self.help()

        return response

    def quote(self):
        text_file = open("quotes.txt")
        list = text_file.readlines()
        return random.choice(list)

    def hello(self):
        return "Hello"

    def help(self):
        response = "Currently I support the following commands:\r\n"

        for command in self.commands:
            response += command + "\r\n"

        return response