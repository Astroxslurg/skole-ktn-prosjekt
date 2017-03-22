from ResponseGenerator import ResponseGenerator

"""
General Helpers
"""

def isRequestValid(request, expectedType):
    requestIsAsExpect = request["request"] == expectedType
    if requestIsAsExpect is False:
        raise ValueError("request was not: " + expectedType)


"""
Login helpers
"""

def takenUsernameError():
    data = {
        'response': "error",
        'content': "That name is taken",
        'sender': "server"
    }
    return ResponseGenerator(data).jsonPayload()


def invalidUsernameError():
    data = {
        'response': "error",
        'content': "username contains unsupported characters, " +
        "please use only letters A-Z, a-z and numbers 0-9",
        'sender': "server"
    }
    return ResponseGenerator(data).jsonPayload()


def isUsernameTaken(username, state):
    return username in state.getUsernames()


def isUsernameInvalid(username):
    for c in username:
        if not ((47 < ord(c) < 58)
           or (64 < ord(c) < 91)
           or (96 < ord(c) < 123)):
            return True
    return False


def loginSuccessful():
    data = {
        'response': "info",
        'content': "Login successful",
        'sender': "server"
    }
    return ResponseGenerator(data).jsonPayload()


class Features():
    def __init__(self, state, currentConnection):
        self.state = state
        self.currentConnection = currentConnection
        self.authorized_requests = {
            'logout': self.logout,
            'login': self.login,
            'msg': self.msg,
            'help': self.help,
            'names': self.names,
        }
        self.open_requests = {
            'help': self.help,
            'login': self.login,
        }

    def login(self, request):
        isRequestValid(request, "login")
        username = request["content"]

        if isUsernameInvalid(username):
            return invalidUsernameError()

        if isUsernameTaken(username, self.state):
            return takenUsernameError()

        self.state.addUsername(username, self.currentConnection)

        return self.history(request)

    def msg(self, request):
        isRequestValid(request, 'msg')
        data = {
            'sender': self.state.getCurrentUsername(self.currentConnection),
            'response': 'message',
            'content': request["content"],
        }
        self.state.addMsg(data)

        return 'BROADCAST'

    def help(self, request):
        commands = """
        Commands available at all times:
            'help': Shows this help-menu
            'login': Logs you into the chat client

        Commands only available after logging in:
            'logout': Logs you out again
            'names': Lists all current usernames
            'msg': Sends a message to all clients
        """
        data = {
            'response': "info",
            'content': commands,
            'sender': "server"
        }
        jsonResponse = ResponseGenerator(data).jsonPayload()

        return jsonResponse

    def names(self, request):
        data = {
            'response': 'info',
            'content': self.state.getUsernames(),
            'sender': 'server'
        }
        jsonResponse = ResponseGenerator(data).jsonPayload()
        return jsonResponse

    def logout(self, request):
        self.state.removeUsernameFromConnection(self.currentConnection)
        data = {
            'response': 'info',
            'content': 'Logout successful',
            'sender': 'server'
        }
        return ResponseGenerator(data).jsonPayload()

    def history(self, request):
        history = self.state.getHistory()
        data = {
            'response': 'history',
            'sender': 'server',
            'content': history
        }

        return ResponseGenerator(data).jsonPayload()

    def noSuchMethod(self):
        data = {
            'sender': "server",
            'response': "error",
            'content': "There is no such command, " +
            "or you do not have sufficient privileges"
        }
        return ResponseGenerator(data).jsonPayload()
