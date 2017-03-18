# -*- coding: utf-8 -*-
import socketserver
import json
from RequestHandler import RequestHandler
from ResponseGenerator import ResponseGenerator
"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

class State:
    def __init__(self):
        self.history = []
        self.connections = {}

    def addConnection(self, clientConnection):
        # use the port as an identifier
        connectionIdentifier = clientConnection.getpeername()[1]
        self.connections[connectionIdentifier] = {
            'connection': clientConnection,
            'username': None,
            }

    def getConnections(self):
        return [value["connection"] for key, value in self.connections.items()]

    def getCurrentConnectionEntry(self, currentConnection):
        connectionIdentifier = currentConnection.getpeername()[1]
        return self.connections[connectionIdentifier]

    def getUsernames(self):
        return [value["username"] for key, value in self.connections.items()]

    def getCurrentUsername(self, clientConnection):
        return [
            value["username"] for key, value in self.connections.items()
            if key == clientConnection.getpeername()[1]
            ][0]

    def isUserLoggedIn(self, connection):
        return not not self.getCurrentUsername

    def addMsg(self, payload):
        self.history.append(payload)

        for connection in self.getConnections():

            # execute and generate response (JSON formatted)
            jsonResponse = ResponseGenerator(payload).jsonPayload()

            # send response
            connection.send(bytes(jsonResponse, "ascii"))

    def getHistory(self):
        return self.history

    def addUsername(self, username, currentConnection):
        connectionEntry = self.getCurrentConnectionEntry(currentConnection)
        connectionEntry["username"] = username


state = State()

class ClientHandler(socketserver.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request

        print(self.connection)
        state.addConnection(self.connection)

        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            # TODO: Add handling of received payload from client

            # Convert payload from JSON to object
            payloadToData = json.loads(received_string)

            # determine what request is being made
            request_handler = RequestHandler(payloadToData,
                                             state,
                                             self.connection)

            # execute and generate response (JSON formatted)
            jsonResponse = request_handler.callHandler()

            if not jsonResponse == 'BROADCAST':
                # send response
                self.connection.send(bytes(jsonResponse, "ascii"))


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True


if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """
    HOST, PORT = 'localhost', 9998
    print ('Server running...')

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
