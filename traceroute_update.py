import os
import struct , socket
import sys ,time ,select
from struct import *
import re

dst = sys.argv[1]
regex = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
result = regex.match(dst)

try :
	dst_name=socket.gethostbyaddr(dst)[0]
	if not result:
		ds_name=socket.gethostbyaddr(dst)[2]
		dst_name=''.join(ds_name)
except socket.gaierror:
	print "Invalid address !"
	sys.exit()
except socket.herror:
	print "invalid IPV4 Address Or Unreachable ! \n"
	dst_name=dst
	pass

print("Traceroute to %s %s  ,30 hops max" %(dst,dst_name))
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
#icmp header	

i =1
while  i <= 30 :
	sock =socket.socket(socket.AF_INET, socket.SOCK_RAW ,1)
	sock.setsockopt(socket.SOL_IP, socket.IP_TTL,i)
	sock.settimeout(2)
	print""
	sys.stdout.write("%d   " %i)
	s=0
	while s < 3 :
		s += 1		
		icmp_type =  8
		icmp_code =  0
		icmp_sum  =  0
		icmp_id   =  1
		icmp_seq  =  s

		icmp_header=struct.pack('!BBHHH', icmp_type, icmp_code, icmp_sum, icmp_id, icmp_seq)	
		psh=icmp_header;
		icmp_sum =checksum(psh)
		icmp_header2=struct.pack('!BBHHH', icmp_type, icmp_code, icmp_sum, icmp_id, icmp_seq)
		icmp_packet=icmp_header2
		send_time=time.time()
		sock.sendto(icmp_packet ,(dst,1))
		try:		
			ic_packet ,addr=sock.recvfrom(1024)
			recv_time=time.time()
			time_def=recv_time-send_time
			time_out = round(time_def * 1000,3)
			c_addr=addr[0]
			try :
				c_name=socket.gethostbyaddr(c_addr)[0]
			except socket.error:	
				c_name=c_addr			
		        sys.stdout.write("%s  (%s ms)  " % (c_name ,time_out))
			sock.close
			if c_name == dst_name or addr[0] == dst_name :
				print dst_name
				sys.exit()	
		except KeyboardInterrupt :
			sys.exit()		
		except socket.timeout  :
			sys.stdout.write("*    ")
	
	sock.close()
	i += 1
	
	




































 
