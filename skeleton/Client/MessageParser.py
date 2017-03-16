import json

class MessageParser():
    def __init__(self):
        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
	    # More key:values pairs are needed
        }

    def parse(self, payload):
        payload = json.loads(payload)

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            print("Error: Invalid response type." +
                  "There is no parser for response type called" +
                  payload['response'])

    def parse_error(self, payload):
        print(payload)

    def parse_info(self, payload):
        print(payload)

    # Include more methods for handling the different responses...
