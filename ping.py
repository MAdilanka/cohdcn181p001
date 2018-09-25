import os
import struct , socket
import sys ,time ,select
from struct import *
import re

dst =sys.argv[1]
regex = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
result = regex.match(dst)
dst_name=dst
if not result:
	try:
		dst_name=socket.gethostbyaddr(dst)[2]
		dst_name=''.join(dst_name)
	except socket.gaierror:
		print "Invalid address !"
		sys.exit()
	except socket.herror:
		print "invalid Address! \n"
		sys.exit()
	
sock =socket.socket(socket.AF_INET, socket.SOCK_RAW ,1)
sock.settimeout(5)

socktcp = socket.socket(socket.AF_PACKET,socket.SOCK_RAW, socket.htons(0x0800))
socktcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socktcp.settimeout(5)
	
def checksum(source_string):
    sum = 0
    countTo = (len(source_string)/2)*2
    count = 0
    while count<countTo:
        thisVal = ord(source_string[count + 1])*256 + ord(source_string[count])
        sum = sum + thisVal
        sum = sum & 0xffffffff 
        count = count + 2
    if countTo<len(source_string):
        sum = sum + ord(source_string[len(source_string) - 1])
        sum = sum & 0xffffffff 
    sum = (sum >> 16)  +  (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer
print ("\nPinging %s . . . . \n" %(dst_name))
i=0
f=0
try :
	while i<4 :
		i+=1

		dest_ip =dst_name
		src_ip ='192.168.225.128'
		#icmp header	
		icmp_type =  8
		icmp_code =  0
		icmp_sum  =  0
		icmp_id   =  1
		icmp_seq  =  i	

		icmp_header=struct.pack('!BBHHH', icmp_type, icmp_code, icmp_sum, icmp_id, icmp_seq)	
		psh=icmp_header;

		icmp_sum =checksum(psh)
		icmp_header2=struct.pack('!BBHHH', icmp_type, icmp_code, icmp_sum, icmp_id, icmp_seq)
		packet=icmp_header2

		send_time=time.time()
		try :
			sock.sendto(packet ,(dest_ip,1))
			icmp_packet ,addr=sock.recvfrom(1024)
		except socket.gaierror:
			print "Invalid IPV4 Address!"
			sys.exit()			
		except socket.timeout :
			print 'Requested Time Out'
			f+=1
			v=i-f
			p=(f/i)*100
			continue
		recv_time =time.time()
		icmp_header=icmp_packet[20:28]
		icmp = unpack('!BBHHH' ,icmp_header)
		ip_packet=socktcp.recvfrom(1024)
		ip_packet = ip_packet[0]
		ip_header=ip_packet[14:34]
		iph = unpack('!BBHHHBBH4s4s' ,ip_header)
		time_taken=recv_time-send_time
	
		time_out = round(time_taken * 1000,1)
			
		if icmp[0] == 3 :
			print '%s : Destination unreachable !'%(dst)
			f+=1
			v=i-f
			p=(f/i)*100
			continue

		elif socket.inet_ntoa(iph[8]) == dst_name :
			print ("%s bytes from: %s: icmp_seq =%s ttl =%s %s ms" %((len(packet)),socket.inet_ntoa(iph[8]) ,icmp[4] ,iph[5] ,time_out))
		else :
			i-=1
			continue
		time.sleep(1)
		v=i-f
		p=(i-v)*100
	print ("-------- %s Ping Statistics ---------"%(dst))
	print ("%s packets Transmited   %s packets recieved %.2f packet loss "%(i ,v,p))
	sys.exit()
except KeyboardInterrupt :
	print ("-------- %s Ping Statistics ---------"%(dst))
	print ("%s packets Transmited   %s packets recieved %.2f packet loss "%(i ,v,p))
	sys.exit()


	
        

