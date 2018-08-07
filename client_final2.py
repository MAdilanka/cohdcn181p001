import socket ,sys ,os
import threading 
try:
	host = "192.168.225.128"
	port = 8080
	sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))
	print 'server connected '
	print "Press 'q' to Exit Program \n\n"

        def client_recieve():
		while True:
			data = sock.recv(1024)
			if data =='q':
				sock.close()
				print '\n.....chat closed......'
				os._exit(1)
			else :
				print "\nserver : " ,data
			if not data :
				break
	def client_send():
		while True:
			send_data=raw_input("\nclient : ")
			sock.send(send_data)
			if send_data=="q" :
					print "\n.....chat closed......"
					sock.close()
					os._exit(1)

	threadc_send = threading.Thread(target = client_send)
	threadc_send.start()

	threadc_recieve = threading.Thread(target = client_recieve)
	threadc_recieve.start()
except socket.error :
		print "\n ! server not started. . connection refused !"
		sys.exit(0)	
	

