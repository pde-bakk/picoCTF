# Scavenger_Hunt

Again? This feels familiar.

First part is in the page source: `picoCTF{t`.
Second part is in mycss.css: `h4ts_4_l0`
The third part is not in the myjs.js this time, but it does contain a hint: `/* How can I keep Google from indexing my website? */`, the answer?

http://mercury.picoctf.net:27393/robots.txt

```
Part 3: t_0f_pl4c
I think this is an apache server... can you Access the next flag?
```

Not done yet, we should check http://mercury.picoctf.net:27393/.htaccess too:
```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```
Next hint: .DS_Store, how I hate that file, but not this time.
`Congrats! You completed the scavenger hunt. Part 5: _d375c750}`

All together: `picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_d375c750}`
