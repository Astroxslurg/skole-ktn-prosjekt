import json

class MessageParser():
    def __init__(self):
        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history,
        }

    def parse(self, payload):
        payload = json.loads(payload)

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            print("Error: Invalid response type. " +
                  "There is no response type called " +
                  payload['response'])

    def parse_message(self, payload):
        print(payload['sender'] + ': ' + payload["content"])

    def parse_error(self, payload):
        print('Error: ' + payload['content'])

    def parse_info(self, payload):
        print(payload['content'])

    def parse_history(self, payload):
        print("Login successful!")
        for message in payload['content']:
            self.parse_message(message)

    # Include more methods for handling the different responses...
