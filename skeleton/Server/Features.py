from ResponseGenerator import *

class Features():
	def __init__(self, state):
		self.state = state	
	
	def login(self, request):
			print("hei")
			
	def msg(self, request):
		print("hei")
		
	def help(self, request):
		data = {
			'response': "info",
			'content': "Help is here!",
			'sender': "server"
		}
		json = ResponseGenerator(data).jsonPayload()
		
		return json
		
		
	def logout(self, request):
		print("hei") 
		
	def	noSuchMethod():
			
			data = {
				sender: "server",
				response: "Error",
				content: "There is no such command"
			}
			return ResponseGenerator(data)
					