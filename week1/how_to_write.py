with open('test.txt', 'w') as f:	#must use 'w', if the txt file does not exist, then created
	f.write('Hello, World!')
with open('test.txt') as f:
	p1 = f.read(5)
	print(p1)	#print 'Hello'
	p2 = f.read()
	print(p2)	#print ', World!'

#with can replace open(), close()