from Features import Features


class RequestHandler():

    def __init__(self, data, state, currentConnection):
        features = Features(state, currentConnection)
        self.possible_requests = {
            'login': features.login,
            'logout': features.logout,
            'msg': features.msg,
            'help': features.help,
            'names': features.names
        }
        self.data = data
        self.noSuchMethod = Features(state, currentConnection).noSuchMethod

    def callHandler(self):
        request = self.data["request"]
        if request in self.possible_requests:

            return self.possible_requests[request](self.data)

        else:

            return self.noSuchMethod()
