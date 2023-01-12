# Information

it's a nice picture of a cat,
but if we run `exiftool cat.jpg` we see a suspicious looking License.

```shell
$ echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
picoCTF{the_m3tadata_1s_modified}
```
