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


def addUsername(state, ):
    state.connections


def loginSuccesful():
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

        if isUsernameTaken(username):
            return loginError()

        addUsername(username, state)

        return loginSuccessful()

    def msg(self, request):
        isRequestValid(request, 'msg')
        data = {
            'sender': '<USER>',
            'response': 'message',
            'content': request["content"],
        }
        json = ResponseGenerator(data).jsonPayload()

        return json

    def help(self, request):
        data = {
            'sender': "server",
            'response': "info",
            'content': "Help is here!",
        }
        json = ResponseGenerator(data).jsonPayload()

        return json

    def names(self, request):
        data = {
            'response': 'info',
            'content': state['usernames'],
            'sender': 'server'
        }
        json = ResponseGenerator(data).jsonPayload()
        return json

    def logout(self, request):
        print("hei")

    def noSuchMethod():

        data = {
            sender: "server",
            response: "Error",
            content: "There is no such command"
        }
        return ResponseGenerator(data)
