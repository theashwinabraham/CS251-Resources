#! /bin/bash
# AUTHOR: ASHWIN ABRAHAM

IMAGES=${1-"images"}

ls $IMAGES | { while read x; do { echo "$x" | awk 'BEGIN {
    FS="_"
}

{
    split($2, time_stamp, "-")
    printf "%s-%s-20%s_%s\n", time_stamp[2], time_stamp[3], time_stamp[1], $3
}' | while read y; do mv "$IMAGES/$x" "$IMAGES/$y"; done; } done; }