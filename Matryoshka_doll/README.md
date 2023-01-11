# Matryoshka dolls

```shell
$ unzip dolls.jpg 
Archive:  dolls.jpg
warning [dolls.jpg]:  272492 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/2_c.jpg     
$ unzip base_images/2_c.jpg 
Archive:  base_images/2_c.jpg
warning [base_images/2_c.jpg]:  187707 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/3_c.jpg     
$ unzip base_images/3_c.jpg 
Archive:  base_images/3_c.jpg
warning [base_images/3_c.jpg]:  123606 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/4_c.jpg     
$ unzip base_images/4_c.jpg
Archive:  base_images/4_c.jpg
warning [base_images/4_c.jpg]:  79578 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: flag.txt                
$ unzip base_images/4_c.jpg
$ cat flag.txt 
picoCTF{96fac089316e094d41ea046900197662}
```

bada boom.
