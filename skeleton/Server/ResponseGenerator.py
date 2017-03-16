class ResponseGenerator():
	def __init__(self, data):
		print("ResponseGenerator in town!")
		self.sender = data.sender
		self.response = data.response
		self.content = data.content
		self.timestamp = self.timestamp
		
	def timestamp():
		return "Partytime!"
	
	def payload(self):
		return {
			sender: self.sender,
			response: self.response,
			content: self.content,
			timestamp: self.timestamp
		};
		
	def jsonPayload():
		return json.dumps(self.payload())
		
	 