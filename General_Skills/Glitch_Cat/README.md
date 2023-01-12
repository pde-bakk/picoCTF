# Glitch_Cat

The flag printing service has started glitching!
Let's see what's going on.

```shell
$ nc saturn.picoctf.net 53933
'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
```

It spits out the python code.

```shell
$ nc saturn.picoctf.net 53933 | python3 -c "print(eval(inpu
t()))"
picoCTF{gl17ch_m3_n07_a4392d2e}
```

Or even easier, actually, we can run print it with the interpreter.
```shell
$ nc saturn.picoctf.net 53933 | python3 -i
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 'picoCTF{gl17ch_m3_n07_a4392d2e}'
>>> 
```
