# Nice netcat...

No need for pesky newlines
```shell
$ nc mercury.picoctf.net 22342 | tr '\n' ','
112 ,105 ,99 ,111 ,67 ,84 ,70 ,123 ,103 ,48 ,48 ,100 ,95 ,107 ,49 ,116 ,116 ,121 ,33 ,95 ,110 ,49 ,99 ,51 ,95 ,107 ,49 ,116 ,116 ,121 ,33 ,95 ,53 ,102 ,98 ,53 ,101 ,53 ,49 ,100 ,125 ,10 ,
$
```

They look like ascii values, let's convert them to characters.
```python
arr = [112 ,105 ,99 ,111 ,67 ,84 ,70 ,123 ,103 ,48 ,48 ,100 ,95 ,107 ,49 ,116 ,116 ,121 ,33 ,95 ,110 ,49 ,99 ,51 ,95 ,107 ,49 ,116 ,116 ,121 ,33 ,95 ,53 ,102 ,98 ,53 ,101 ,53 ,49 ,100 ,125 ,10]
s = ''
for i in arr:
	s += chr(i)
print(s)
```
`picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}`
