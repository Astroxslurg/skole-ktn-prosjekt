import json

class ResponseGenerator():
	def __init__(self, data):
		
		self.sender = data["sender"]
		self.response = data["response"]
		self.content = data["content"]
		self.timestamp = self.getTimestamp
		
	def getTimestamp(self):
		return "Partytime!"
	
	def payload(self):
		return {
			'sender': self.sender,
			'response': self.response,
			'content': self.content,
			'timestamp': self.timestamp()
		};
		
	def jsonPayload(self):
		return json.dumps(self.payload())
		
	 