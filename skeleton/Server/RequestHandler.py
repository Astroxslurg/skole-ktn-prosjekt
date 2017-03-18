from Features import Features


class RequestHandler():

    def __init__(self, data, state, currentConnection):

        self.possible_requests = {
            'login': Features(state, currentConnection).login,
            'logout': Features(state, currentConnection).logout,
            'msg': Features(state, currentConnection).msg,
            'help': Features(state, currentConnection).help
        }
        self.data = data
        self.noSuchMethod = Features(state, currentConnection).noSuchMethod

    def callHandler(self):
        request = self.data["request"]
        if request in self.possible_requests:

            return self.possible_requests[request](self.data)

        else:

            return self.noSuchMethod()
