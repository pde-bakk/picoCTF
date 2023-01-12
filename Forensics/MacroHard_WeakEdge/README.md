# MacroHard_WeakEdge

A lot of work went into getting aspose.slides to work, since it relies on an openssl version and wasn't compatible on my system.
In a docker container with OpenSSL version 1.0 it does work, but it just shows that the macro does not contain the flag:
```vba
; $ python3 extract_macros.py Forensics\ is\ fun.pptm
Module1
Attribute VB_Name = "Module1"
Sub not_flag()
    Dim not_flag As String
    not_flag = "sorry_but_this_isn't_it"
End Sub
```

Two interesting files pop up when we unzip the powerpoint file:
ppt/slideMasters/hidden
ppt/vbaProject.bin

running strings on the .bin file doesn't provide us with much.
But catting the 'hidden' file shows us a bunch of characters. Looks like base64?

```shell
$ cat ppt/slideMasters/hidden | tr -d ' ' | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}base64: invalid input
```
(It prints invalid output, because there are supposed to be two trailing ='s after the base64 string.)
