
data=[]
while True :
	value=raw_input("Enter Number : \t")
	if value.isdigit()==True:
		data.append(value)
		i=map(int,data)
		b=sum(i)
	elif value == "" :
		break
print 'Sum of Numbers = ' ,b
print 'list of Nubers = ' ,i



