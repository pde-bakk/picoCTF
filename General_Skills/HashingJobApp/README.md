# HashingJobApp

The program will throw 3 different strings at you, which you have to hash using md5.
Just open a different terminal and use md5sum.

```shell
$ echo -n 'Helen Keller' | md5sum
c0aac1554fe46e67f218df124c318054  -
$ echo -n 'school cafeteria' | md5sum
3e06bd96dca5d429a2e06b3ea613eb41  -
$ echo -n 'a morgue' | md5sum
1c5d1684ae8cd2f62a070044e5fc40c7  -
```

```shell
$ nc saturn.picoctf.net 63116
Please md5 hash the text between quotes, excluding the quotes: 'Helen Keller'
Answer: 
c0aac1554fe46e67f218df124c318054
c0aac1554fe46e67f218df124c318054
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'school cafeteria'
Answer: 
3e06bd96dca5d429a2e06b3ea613eb41
3e06bd96dca5d429a2e06b3ea613eb41
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'a morgue'
Answer: 
1c5d1684ae8cd2f62a070044e5fc40c7
1c5d1684ae8cd2f62a070044e5fc40c7
Correct.
picoCTF{4ppl1c4710n_r3c31v3d_bf2ceb02}
```
