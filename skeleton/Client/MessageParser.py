import json

class MessageParser():
    def __init__(self):
        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            # More key:values pairs are needed
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
        print(payload)

    def parse_info(self, payload):
        print(payload['content'])

    # Include more methods for handling the different responses...
