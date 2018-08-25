import socket 
import sys
from struct import *
from binascii import hexlify

sock = socket.socket(socket.AF_PACKET,socket.SOCK_RAW, socket.htons(0x0800))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('ens33', 0))



while True:
	
	packet=sock.recvfrom(65565)
	packet = packet[0]
	ip_header=packet[14:34]
	iph = unpack('!BBHHHBBH4s4s' ,ip_header)
		
	eth_header=packet[0:14]
	eth = unpack('!6s6sH' ,eth_header)

	icmp_header=packet[34:42]
	icmp = unpack('!BBHHH' ,icmp_header)

	tcp_hed = packet[34:54]
	tcp = unpack('!HHIIHHHH',tcp_hed)

	udp_hed = packet[34:42]
	udp = unpack('!HHHH' ,udp_hed)


	print '\nVersion        :' ,iph[0]>> 4
	print 'Ip Header Length :' ,iph[0]& 0xF
	print 'TTL 		:' ,iph[5] 
	print 'Protocol 	:' ,iph[6] 
	print 'source IP Address:' ,socket.inet_ntoa(iph[8]);
	print 'Dest addr	:' ,socket.inet_ntoa(iph[9]);

	print 'Source Mac 	:',hexlify(eth[0])
	print 'Destination Mac  :' ,hexlify(eth[1])
	print 'TYPE		:' ,eth[2]

	if iph[6] == 1 :
		print '\n\t\ticmp packet'
		print'Type   :',icmp[0]
		print'Code   :',icmp[1]
		print'csum   :',icmp[2]
		print'ID     :',icmp[3]
		print'Seq Num:',icmp[4]
		print'.........................\n'
	elif iph[6] == 6 : 

		print '\n\t\t TCP Header'
		print 'S.Port	     :' ,tcp[0]
		print 'D.Port	     :' ,tcp[1]
		print 'Seq.Number    :' ,tcp[2]
		print 'Ack.Number    :' ,tcp[3]
		print 'Offset	     :'	,tcp[4]>> 4
		print 'Reserved      :' ,tcp[4] >> 7
		print 'Fragment      :' ,tcp[4] & 0XF
		print 'Window Size   :' ,tcp[5]
		print 'Checksum      :' ,tcp[6]
		print 'Urgent pointer:' ,tcp[7]
		print'.........................\n'
	
	elif iph[6] == 17 :
		
		print '\n\t\tUDP Header'
		print 'source port : ',udp[0]
		print 'Dest.Port   : ',udp[1]
		print 'Length      : ',udp[2]
		print 'checksum    : ',udp[3]
		print '.........................\n'
		





















