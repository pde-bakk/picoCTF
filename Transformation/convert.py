#!/usr/bin/env python3

s = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽'

res=''
for i in range(len(s)):
	a = chr(ord(s[i])>>8)
	b = chr((ord(s[i]))-((ord(s[i])>>8)<<8))
	res += a+b

print(res)
