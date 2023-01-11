# tunn3l_v1s10n

You can download the file from https://mercury.picoctf.net/static/09a86202e72dbdb5bf4d1b5d2c6a5b86/tunn3l_v1s10n

I won't link it here, because it is almost 3MB.

```shell
$> hexdump tunn3l_v1s10n | head 
0000000 4d42 268e 002c 0000 0000 d0ba 0000 d0ba
```
The first 2 bytes are the headerfield, 0x42 0x4D = BM for Bitmap.
The next 4 bytes are the filesize. 0x002c268e = 2893454 (matches with the output of ls -la).
The next 2x2 bytes are reserved. Here they're both 0.
The last 4 bytes are the offset, i.e. the starting address: 0xd0ba = 53434, rather large for an offset.

After that we change the bad value for the DIB Header size and change the height.

We can edit the byte content of the file by piping the output of xxd to a file, editing its contents and using `xxd -r hex.txt > image.bmp` to generate a binary from it again.
