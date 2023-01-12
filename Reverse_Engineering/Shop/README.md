# Shop

Well, this shop seems to store its counts as signed integers, so if you sell -1 * MAX_INT of your Fruitful Flags, you can obtain many flags and get money.
Then, you can buy the entire market supply of the Fruitful Flags and the market spits out the flag to you.
`Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 98 56 100 55 50 55 49 102 125]`

```python
s = ''
flag_values = [112, 105, 99, 111, 67, 84, 70, 123, 98, 52, 100, 95, 98, 114, 111, 103, 114, 97, 109, 109, 101, 114, 95, 98, 56, 100, 55, 50, 55, 49, 102, 125]
for i in flag_values:
	s += chr(i)
print(s)
```

`picoCTF{b4d_brogrammer_b8d7271f}`
