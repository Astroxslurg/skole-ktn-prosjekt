# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser


class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        self.host = host
        self.server_port = server_port

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # TODO: Finish init process with necessary code

        self.userCommands = {
            'help': self.help,
        }

        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        print("running....")

    def disconnect(self):
        # TODO: Handle disconnection
        pass

    def receive_message(self, message):
        # TODO: Handle incoming message
        pass

    def send_payload(self, data):
        # TODO: Handle sending of a payload
        pass

    def parseCommands(self, payload):
        if payload in self.userCommands:
            return self.userCommands[payload]()
        else:
            print("Error: Invalid command." +
                  " There is no command called " + payload)

    def help(self):
        print("This is the help menu")
        message = json.dumps({
            'request': 'help',
        })
        print(message)
        self.connection.send(message)


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
    while True:
        client.parseCommands(input())
