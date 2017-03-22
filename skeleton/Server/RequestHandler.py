from Features import Features


class RequestHandler():

    def __init__(self, data, state, currentConnection):
        self.features = Features(state, currentConnection)
        self.data = data
        self.noSuchMethod = Features(state, currentConnection).noSuchMethod
        self.state = state
        self.currentConnection = currentConnection

    def callHandler(self):
        request = self.data["request"]
        if self.state.isUserLoggedIn(self.currentConnection):
            if request in self.features.authorized_requests:
                return self.features.authorized_requests[request](self.data)
            else:
                return self.noSuchMethod()
        else:
            if request in self.features.open_requests:
                return self.features.open_requests[request](self.data)
            else:
                return self.noSuchMethod()
