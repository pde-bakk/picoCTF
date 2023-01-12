# PW_Crack_4

Same approach as level 3, except now we get the valid hash value from level4.hash.bin using xxd and do a comparison for each hashed password.
And if it matches, print and break

```shell
$ py find_pw.py 
s= 607a, md5sum= 9f040646d73ef4be221ce0df30046625
$ py level4.py 
Please enter correct password for flag: 607a
Welcome back... your flag, user:
picoCTF{fl45h_5pr1ng1ng_d770d48c}
```
