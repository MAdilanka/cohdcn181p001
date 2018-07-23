y=raw_input("enter file name :\t")

f=open(y,'r')
vari=f.read().replace('\n','.').replace('\t','.')
x=vari
parts = [x[i:i+16] for i in range(0,len(x),16)]
print('\n'.join(map(str, parts)))
print('\n')


hexa=vari.encode('hex')
z=hexa
hexparts = [z[j:j+4] for j in range(0,len(z),4)]
b = ' '.join(map(str,hexparts))

chunk, chunk_size = len(b), len(b)//10
y=[b[k:k+chunk_size] for k in range(0, chunk, chunk_size)]
for ele in y:
	print ele














	


