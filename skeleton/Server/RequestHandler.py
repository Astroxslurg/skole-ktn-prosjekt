from Features import Features


class RequestHandler():

    def __init__(self, data, state, currentConnection):
        features = Features(state, currentConnection)
        self.authorized_requests = {
            'logout': features.logout,
            'login': features.login,
            'msg': features.msg,
            'help': features.help,
            'names': features.names,
        }
        self.open_requests = {
            'help': features.help,
            'login': features.login,
        }
        self.data = data
        self.noSuchMethod = Features(state, currentConnection).noSuchMethod
        self.state = state
        self.currentConnection = currentConnection

    def callHandler(self):
        request = self.data["request"]
        if self.state.isUserLoggedIn(self.currentConnection):
            if request in self.authorized_requests:
                return self.authorized_requests[request](self.data)
            else:
                return self.noSuchMethod()
        else:
            if request in self.open_requests:
                return self.open_requests[request](self.data)
            else:
                return self.noSuchMethod()
