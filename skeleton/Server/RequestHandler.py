from ResponseGenerator import *
class RequestHandler():

	def __init__(self, data):
		print("RequestHandler represent'! ")
		
		self.possible_requests = {
			'login': self.login,
			'logout': self.logout,
			'msg': self.msg,
			'help': self.help
			}
		self.data = data
		print(data)
		
		
	def	callHandler(self):
		request = self.data["request"]
		if request in self.possible_requests:
			
		 return self.possible_requests[request](self.data)

		else:
			
			return self.noSuchMethod()
	
	def	noSuchMethod():
		
		data = {
			sender: "server",
			response: "Error",
			content: "There is no such command"
		}
		return ResponseGenerator(data)
		
	def login(self, request):
		print("hei")
		
	def msg(self, request):
		print("hei")
		
	def help(self, request):
		data = {
			'response': "OK",
			'content': "Yo!",
			'sender': "server"
		}
		json = ResponseGenerator(data).jsonPayload()
		print(json)
		return json
		
		
	def logout(self, request):
		print("hei")        


