# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser


class Client:
    """
    This is the chat client class
    """

    """
    The isSimulation flag is set to true when running simulations,
    so that the "while True" loop doesn't block execution of simulation script.
    """

    def __init__(self, host, server_port, isSimulation = False):
        """
        This method is run when creating a new Client object
        """

        self.host = host
        self.server_port = server_port
        self.isSimulation = isSimulation

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # TODO: Finish init process with necessary code

        self.userCommands = {
            'h': self.help,
            'help': self.help,
            'login': self.login,
            'logout': self.logout,
            'names': self.names,
        }

        self.messageParser = MessageParser()

        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))

        messageReceiver = MessageReceiver(self, self.connection)
        messageReceiver.start()
        if self.isSimulation is True:
            return None

        print("Welcome to the very best chat client the world has ever seen!")
        self.printClientHelpMessage()

        while True:
            inp = input()
            if inp[0] == '$':
                self.parseCommands(inp[1:].lower())
            else:
                self.sendMessage(inp)

    def disconnect(self):
        # TODO: Handle disconnection
        pass

    def receive_message(self, message):
        self.messageParser.parse(message)

    def send_payload(self, data):
        self.connection.send(bytes(data, "ascii"))

    def parseCommands(self, payload):
        if payload in self.userCommands:
            return self.userCommands[payload]()
        else:
            print("Error: Invalid command." +
                  " There is no command called " + payload)

    def sendMessage(self, inp):
        message = json.dumps({
            'request': 'msg',
            'content': inp,
        })
        self.send_payload(message)

    def names(self):
        message = json.dumps({
            'request': 'names',
        })
        self.send_payload(message)

    def printClientHelpMessage(self):
        print("You type commands by prepending a '$'")
        print("Type '$help' or '$h' for help, and '$login' to login")
        print("You should start by logging in")
        print("A line not starting with a $-symbol will be sent as a message")

    def help(self):
        print("This is the help menu.")
        self.printClientHelpMessage()
        print("retrieving available commands from server:")

        message = json.dumps({
            'request': 'help',
        })
        self.send_payload(message)

    # simUsername is only used during simulations
    def login(self, simUsername=None):

        if simUsername:
            username = simUsername
        else:
            print("Please enter username")
            username = input()

        message = json.dumps({
            'request': 'login',
            'content': username,
        })
        print("thank you, " + username + "! We will try to log you in...")
        self.send_payload(message)

    def logout(self):
        print("Loggin out...")
        message = json.dumps({
            'request': 'logout',
        })
        self.send_payload(message)


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
