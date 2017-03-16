from Features import *

class RequestHandler():

	def __init__(self, data):
		print("RequestHandler represent'! ")
		
		self.possible_requests = {
			'login': Features().login,
			'logout': Features().logout,
			'msg': Features().msg,
			'help': Features().help
			}
		self.data = data
		self.noSuchMethod = Features.noSuchMethod
		
		
	def	callHandler(self):
		request = self.data["request"]
		if request in self.possible_requests:
			
		 return self.possible_requests[request](self.data)

		else:
			
			return self.noSuchMethod()
	
	
	       


