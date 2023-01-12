# PW_Crack_3

I used bvi to inspect the contents of level3.hash.bin
And then, in `find_pw.py`, I hash each of the possible passwords to see if they match, and 'dba8' matches.

```shell
$ py level3.py                                                    
Please enter correct password for flag: dba8
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
```
