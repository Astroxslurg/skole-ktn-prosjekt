# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser
from CommandReceiver import CommandReceiver


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
            'help': self.help,
            'login': self.login,
            'logout': self.logout,
        }

        self.messageParser = MessageParser()

        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))

        messageReceiver = MessageReceiver(self, self.connection)
        messageReceiver.start()

        while True and not self.isSimulation:
            self.parseCommands(input())

    def disconnect(self):
        # TODO: Handle disconnection
        pass

    def receive_message(self, message):
        print(message)
        self.messageParser.parse(message)

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
        
        message = json.dumps({
            'request': 'help',
        })
        self.connection.send(bytes(message, "ascii"))

    def login(self, simUsername = None):

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
        self.connection.send(bytes(message, "ascii"))

    def logout(self):
        print("Loggin out...")
        message = json.dumps({
            'request': 'logout',
        })
        self.connection.send(bytes(message, "ascii"))


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
