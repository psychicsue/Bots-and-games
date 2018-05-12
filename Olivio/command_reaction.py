class CommandReaction(object):
    def __init__(self):
        self.reaction_command = {
            "users": self.get_users
        }

    def handle_reaction_command(self, command):
        response = ""

        if command in self.reaction_command:
            response += self.reaction_command[command]()
        else:
            response += "Sorry I don't understand the command: " + command + ". "

        return response

    def get_users(self):
        return "USERUSERUSER"
