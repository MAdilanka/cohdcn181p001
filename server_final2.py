import socket, threading, sys ,os
try :
	host = sys.argv[1]
	port = int(sys.argv[2])
	sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((host, port))
	sock.listen(1)
	print 'waiting for a connection'
	conn, client =  sock.accept()
	print client
	print "client connected "
	
	def send():
		while True:
			server_send=raw_input('\nserver :')
			conn.send(server_send)
	
	thread_send = threading.Thread(target = send)
	thread_send.daemon = True
	thread_send.start()
except KeyboardInterrupt:
			sys.exit()
while True:
	try:
		data = conn.recv(1024) 
		print '\nClient :' ,data	
		
	except KeyboardInterrupt:
			conn.close()
			sys.exit()
	else:
		if not data :
			break	
	

