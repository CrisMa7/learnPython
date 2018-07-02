#!/usr/bin/env python3
# -*- coding: utf-8 -*-
str_age = input('please input your age: ')
age = int(str_age)
if age >= 18:
	print('your age is', age)
	print('adult')
elif age >= 6:
	print('your age is', age)
	print('teenager')
else:
	print('kid')	
#BMI
height = 1.75
weight = 60.5
bmi = weight/pow(height, 2)
if bmi < 18.5:
	print('too thin')
elif bmi >= 18.5 and bmi < 25:
	print('normal')
elif bmi >= 25 and bmi < 28:
	print('fat')
elif bmi >=28 and bmi < 32:
	print('too fat')
else:
	print('serious fat')

