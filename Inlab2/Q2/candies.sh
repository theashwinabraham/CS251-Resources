#! /bin/bash
# AUTHOR: ASHWIN ABRAHAM
x=0
y=1
str=""
num=$(($1))
for ((i=0; i<$num; i++))
do
    str+="$x "
    temp=$(($x))
    x=$(($y))
    y=$(($y+$temp))
done

echo $str