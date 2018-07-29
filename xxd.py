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
	
		letters=txt.replace('\n','.').replace('\t','.')
		letterblock=[]
		letterblock.append(letters)
		off_set=('%08x'%(offset*16))	
		print('{0}: {1:<39}   {2}'.format (off_set,' '.join(hexablock),' '.join(letterblock)))
		offset+=1

if not os.path.exists(sys.argv[1]):
	print("Wrong Input")
	sys.exit(1)
xxd(sys.argv[1])			
