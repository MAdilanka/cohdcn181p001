import socket ,sys
import threading 

def client_recieve():
	while True:
		data = sock.recv(1024)
		print "\nserver : " ,data
		if not data :
			break
def client_send():
	while True:
		send_data=raw_input("client : ")
		sock.send(send_data)
if __name__ == "__main__" :

	host = "192.168.225.128"
	port = 8080
	sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))
	print 'server connected  \n\n'

	threadc_send = threading.Thread(target = client_send ,args=())
	threadc_send.start()

	threadc_recieve = threading.Thread(target = client_recieve ,args=())
	threadc_recieve.start()

	

