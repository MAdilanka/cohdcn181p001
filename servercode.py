import socket, threading ,sys

def send():
	while True:
		server_send=raw_input('server :')
		conn.send(server_send)
		
def recieve():
	while True:
		data = conn.recv(1024) 
		print '\nClient :' ,data
		if not data:
			break

if __name__ == "__main__" :

	host='192.168.225.128'
	port=8080
	sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((host, port))
	sock.listen(1)
	print 'wait for a connection'
	conn, client =  sock.accept()
	print client
	print "client connected \n \n"


	thread_send = threading.Thread(target = send)
	thread_send.start()

	thread_recieve = threading.Thread(target = recieve)
	thread_recieve.start()


