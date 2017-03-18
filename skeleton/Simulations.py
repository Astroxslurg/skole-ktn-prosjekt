import sys
from threading import Timer
sys.path.insert(0, './Client')
sys.path.insert(0, './Server')

from Client import Client
from Server import ThreadedTCPServer, ClientHandler

# Start the Server
def	startServer():

	HOST, PORT = 'localhost', 9998

	# Set up and initiate the TCP server
	server = ThreadedTCPServer((HOST, PORT), ClientHandler)
	server.serve_forever()

def startClient():
	# Start the Client
	joe = Client('localhost', 9998, True)
	#jimbo = Client('localhost', 9998, True)
	joe.login("Joe")
	# Sim login
	#client.login()


server = Timer(0.0, startServer)

client = Timer(0.1, startClient)

server.start()
client.start()
