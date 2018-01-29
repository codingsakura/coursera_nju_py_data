s = 'Tencent Technology Company Limited'
with open('companies.txt', 'a+') as f:
	f.writelines('\n')	#add a enter at the end of the file
	f.writelines(s)	#add a new line
	f.seek(0)	#relocate at the beginning of the file
	cNames = f.readlines()
	print(cNames)	#read the file from the beginning