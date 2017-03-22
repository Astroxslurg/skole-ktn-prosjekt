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

def loginError():
    data = {
        'response': "error",
        'content': "That name is taken",
        'sender': "server"
    }

    return ResponseGenerator(data).jsonPayload()


def isUsernameTaken(username, state):
    return username in state.getUsernames()


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

    def login(self, request):
        isRequestValid(request, "login")
        username = request["content"]

        if isUsernameTaken(username, self.state):
            return loginError()

        self.state.addUsername(username, self.currentConnection)

        return loginSuccessful()

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
        data = {
            'response': "info",
            'content': "Help is here!",
            'sender': "server"
        }
        json = ResponseGenerator(data).jsonPayload()

        return json

    def names(self, request):
        data = {
            'response': 'info',
            'content': self.state.getUsernames(),
            'sender': 'server'
        }
        json = ResponseGenerator(data).jsonPayload()
        return json

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
            'response': 'info',
            'sender': 'server',
            'content': history
        }

        return ResponseGenerator(data).jsonPayload()

    def noSuchMethod(self):

        data = {
            'sender': "server",
            'response': "Error",
            'content': "There is no such command"
        }
        return ResponseGenerator(data)
