MAX_COOKIE_AMOUNT=30

for i in $(seq 1 $MAX_COOKIE_AMOUNT);
do
	echo "Cookie number $i"
	curl -s http://mercury.picoctf.net:21485/ -H "Cookie: name=$i;" -L | grep -i Flag
done
