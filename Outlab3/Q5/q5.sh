#! /bin/bash

awk -v num=$3 '{
    if(NR == FNR)
    {
        if(NR > 1 && NR <= 1+num)
        {
            split($0, kv_pairs, "-")
            dict[kv_pairs[1]] = kv_pairs[2]
        }
    }
    else
    {
        for(i = 1; i<=NF; i++)
        {
            if($i in dict) printf dict[$i]
            else printf $i

            printf "  "
        }
    }
}' $1 $2