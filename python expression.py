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
	y = re.findall('[0-9]+',z) #look thourgh all the numbers
	for word in y:
		if len(word)>0:
			sum = sum + int(word)
print(sum)

