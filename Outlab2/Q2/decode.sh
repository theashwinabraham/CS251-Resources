#!/bin/bash
# AUTHOR: ASHWIN ABRAHAM

function update_pw()
{
    pattern="#@$"
    word=""
    word_regex="[A-Za-z]+"
    pattern_regex="[\!\@\#\$\%\^\&\*]{3}"
    words_found=0
    prev=""
    prev_prev=""

    while read line
    do
        for x in $line
        do
            #echo "$prev_prev :: $prev :: $x"
            if [ "$words_found" = "0" ]
            then
                if [ "$prev" = "$pattern" ]
                then
                    if [[ $x =~ $word_regex ]]
                    then
                        word="$x"
                        let "words_found += 1"
                    fi
                fi
            elif [ "$words_found" = "$1" ]
            then
                if [ "$prev" = "$word" ]
                then
                    if [[ $x =~ $pattern_regex ]]
                    then
                        pattern="$x"
                        echo "Last Word found: $word"
                        echo "Last Pattern found: $pattern"
                        exit
                    fi
                fi
            else
                if [ "$prev_prev" = "$word" ]
                then
                    if [[ $prev =~ $pattern_regex ]]
                    then
                        if [[ $x =~ $word_regex ]]
                        then
                            pattern="$prev"
                            word="$x"
                            let "words_found += 1"
                        fi
                    fi
                fi
            fi
            prev_prev="$prev"
            prev="$x"
        done
    done
}

cat "$1" | update_pw $2