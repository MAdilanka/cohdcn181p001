x=0
data = []
numbers=[]
while True :
	value=raw_input("Enter Number : \t")
	data.append(value)
	if value.isdigit()==True:
		i=int(value)
		numbers.append(i)
		x=x+i
	elif value == "" :
		break
print'-------------------------------------------------------'
print 'sum of Values :' ,x 
print'-------------------------------------------------------'
print'-------------------------------------------------------'
print "Numbers you have Entered :" ,numbers
print "Your All inputs : " ,data
print'-------------------------------------------------------'

	
	
        
	

	

