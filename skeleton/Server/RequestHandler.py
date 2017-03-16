from Features import *

class RequestHandler():

	def __init__(self, data, state):
		print("RequestHandler represent'! ")
		
		self.possible_requests = {
			'login': Features(state).login,
			'logout': Features(state).logout,
			'msg': Features(state).msg,
			'help': Features(state).help
			}
		self.data = data
		self.noSuchMethod = Features(state).noSuchMethod
		
		
	def	callHandler(self):
		request = self.data["request"]
		if request in self.possible_requests:
			
		 return self.possible_requests[request](self.data)

		else:
			
			return self.noSuchMethod()
	
	
	       


