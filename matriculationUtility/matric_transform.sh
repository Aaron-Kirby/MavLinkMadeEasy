#!/bin/bash

sed -e 's/,,,,//g' -e 's/""//g' -e 's/^\s$//g' -e 's/^,\s*$//g' -e 's/,,,\s$//g' -e 's/"",//g' -e 's/^,//g' -r -e 's/Remaining:.*Compl:0/---\n/g' $1 |
sed -r -e 's/,,.*//g' -e 's/"\* Optional"\s//g' -e 's/Course #.*//g' -e 's/"//g' -e 's/,.,.,\s$//g' | awk 'NF' |
sed -r -e 's/,([A-Z])/\t\1/g' > M.txt

grep -e 'CREDIT HRS' M.txt > CATEGORIES.txt

cat CATEGORIES.txt | while read line
do
    sed -n "/$line/,/---/p" M.txt
done

