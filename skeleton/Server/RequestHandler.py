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
		
		
	def	callHandler(self):
		if	data.request in self.possible_requests:
			
		 return self.possible_requests[data.request](data)

		else:
			
			return self.noSuchMethod()
	
	def	noSuchMethod():
		
		data = {
			sender: "server",
			response: "Error",
			content: "There is no such command"
		}
		return ResponseGenerator(data)
		
	def login(self):
		print("hei")
		
	def msg(self):
		print("hei")
		
	def help(self):
		data = {
			response: "OK",
			content: "Yo!",
			sender: "server"
		}
		json = ResponseGenerator(data).jsonPayload()
		print(json)
		
		
	def logout(self, data):
		print("hei")        


