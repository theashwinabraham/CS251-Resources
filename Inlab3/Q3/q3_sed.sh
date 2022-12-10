#! /usr/bin/bash
# AUTHOR: ASHWIN ABRAHAM

sed 's/\.[^$]/$ /g' $1 | sed 's/\.$//g' | sed 's/$/\:\)/g'
