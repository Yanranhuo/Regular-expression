# regular-expression
#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.

import re

file = input('enter the file name:  ')
if len(file)<1: file = 'test.txt'
fun = open(file)
y = list()
z = list()
sum = 0
for line in fun:
	z = line.rstrip()
	y = re.findall('[0-9]+',z) 
	#look thourgh all the numbers, it returns a list of string, so Y is a list
	for word in y:
		#check all the string in the list
		if len(word)>0:
			#there is some line without numbers, er need to skip those lines
			sum = sum + int(word)
			#cannot add int with str, so need to convert to int
print(sum)

