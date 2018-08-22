import socket ,sys ,os
import threading 

try:
	host = sys.argv[1]
	port = 8080
	sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))
	print 'server connected '
	
	def client_recieve():
		while True:
			send_data=raw_input("\nclient : ")
			sock.send(send_data)

	threadc_recieve = threading.Thread(target = client_recieve)
	threadc_recieve.daemon = True
	threadc_recieve.start()

except KeyboardInterrupt:
		sys.exit()
except socket.error :
		print "\n ! server not started. . connection refused !"
		sys.exit(0)	

while True:
	try:
		data = sock.recv(1024)
		print "\nserver : " ,data		
	except KeyboardInterrupt:
		sock.close()
		sys.exit()
	else:
		if not data :
	

