import socket, threading, sys ,os
try:
	def send():
		while True:
			server_send=raw_input('server :')
			conn.send(server_send)
			if server_send=="q" :
					sock.close()
					print "\n.....chat closed......"
					os._exit(1)
		
	def recieve():
		while True:
			data = conn.recv(1024) 
			print '\nClient :' ,data
			if data == "q":
				sock.close()
				print '\n.....chat closed......'
				os._exit(1)
			if not data:
				break

	if __name__ == "__main__" :
			host='192.168.225.128'
			port=8080
			sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.bind((host, port))
			sock.listen(1)
			print 'waiting for a connection'
			conn, client =  sock.accept()
			print client
			print "client connected "
			print "Press 'q' to Exit Program \n \n"
	
			thread_send = threading.Thread(target = send)
			thread_send.start()

			thread_recieve = threading.Thread(target = recieve)
			thread_recieve.start()

except KeyboardInterrupt:
			print "\nProgram Terminated!"
			sys.exit(0)
except socket.error:
			print "address_already_in_use"
			sys.exit(0)	

	


