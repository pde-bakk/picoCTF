# PW_Crack_2

Check the code for the password:
`if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):`

```shell
python3 -c 'print(chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39))'
4ec9

$ python3 level2.py 
Please enter correct password for flag: 4ec9
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_9701e681}
```
