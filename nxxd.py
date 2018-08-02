import sys
import os.path
def xxd(y):
	f=open(y,'r')
	offset=0
	while True:
		txt=f.read(16)
		if not txt:
			break

		hexa=[]
		for i in txt:
			hexa.append('%02x'%ord(i))
		hexablock=[]
		for n in range (0,len(hexa),2):
			hexablock.append(''.join(hexa[n:n+2]))
	         
		letters=[]
		for l in txt :
			ascii_letters=ord(l)
			if ascii_letters<32 or ascii_letters>127 :
				letters.append('.')
			else :
				letters.append(l)
				
		off_set=('%08x'%(offset*16))	
		print('{0}: {1:<39}   {2}'.format (off_set,' '.join(hexablock),''.join(letters)))
		offset+=1

if not os.path.exists(sys.argv[1]):
	print("Wrong Input")
	sys.exit(1)
xxd(sys.argv[1])			
