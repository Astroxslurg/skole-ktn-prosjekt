# -*- coding: utf-8 -*-
from threading import Thread

class CommandReceiver(Thread):

    def __init__(self, client):
        super(CommandReceiver, self).__init__()

        # Flag to run thread as a deamon
        self.daemon = True

        # TODO: Finish initialization of MessageReceiver
        self.client = client


    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        while True:
            self.client.parseCommands(input())
