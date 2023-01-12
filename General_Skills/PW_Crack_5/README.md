# PW_Crack_5

Same approach as level 4, but now we have to open dictionary.txt for all the possible passwords.

```shell
$ xxd level5.hash.bin
00000000: 1236 50dd 0560 5879 18b3 d771 cf0c 0171  .6P..`Xy...q...q
$ py find_pw.py 
s= 9581, md5sum= 123650dd0560587918b3d771cf0c0171
$ py level5.py 
Please enter correct password for flag: 9581
Welcome back... your flag, user:
picoCTF{h45h_sl1ng1ng_36e992a6}
```
