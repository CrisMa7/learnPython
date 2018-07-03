#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny


#计算方程ax^2 + bx + c = 0的解 
def quadratic(a, b, c):
	if pow(b, 2) - 4*a*c >= 0:
		temp = math.sqrt(pow(b, 2) - 4*a*c)
		x1 = (-b + temp)/(2*a)
		x2 = (-b - temp)/(2*a)
		return x1, x2
	else:
		return "no soulution"
	

