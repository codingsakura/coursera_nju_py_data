with open('companies.txt') as f1:
	cNames = f1.readlines()
	for i in range(0, len(cNames)):
		print(cNames[i])
		cNames[i] = str(i + 1) + ' ' + cNames[i]
		
with open('scompanies.txt', 'w') as f2:
	f2.writelines(cNames)

with open('scompanies.txt') as f3:
	sNames = f3.readlines()
	for i in range(0, len(sNames)):
		print(sNames[i])