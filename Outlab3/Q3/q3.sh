#! /bin/bash

cat $1 | awk -v args="$*" 'BEGIN {
    num = split(args, the_args, " ")
    is_char = 0
    is_word = 0
    is_line = 0
    is_para = 0
    if(num <=1)
    {
        is_char = 1
        is_word = 1
        is_line = 1
        is_para = 1
    }
    else
    {
        for(i = 1; i<=num; ++i)
        {
            if(the_args[i] == "-chars")
            {
                is_char = 1
            }
            if(the_args[i] == "-words")
            {
                is_word = 1
            }
            if(the_args[i] == "-lines")
            {
                is_line = 1
            }
            if(the_args[i] == "-paras")
            {
                is_para = 1
            }
        }
    }

    num_args = is_char + is_word + is_line + is_para

    to_print["-chars"] = "characters"
    to_print["-words"] = "words"
    to_print["-lines"] = "lines"
    to_print["-paras"] = "paragraphs"
    encountered = 0
    count_c = 0
    count_w = 0
    count_l = 0
    count_p = 0
}

{
    if(is_char == 1)
    {
        for(i = 1; i<=NF; ++i)
        {
            count_c += split($i, _, "")
        }
    }
    if(is_word == 1)
    {
        count_w += NF
    }
    if(is_line == 1) { count_l++ }
    if(is_para == 1)
    {
        if(NF > 0 && encountered == 0)
        {
            encountered = 1;
            count_p++
        }
        if(NF == 0) encountered = 0
    }
}

END	{
    ended = 0
    print_c = 0
    print_w = 0
    print_l = 0
    print_p = 0
    printed = 0
    if(is_char == 1)
    {
        printf "%d characters", count_c
        print_c = 1
        ++printed
    }

    if(num_args > printed)
    {
        if(print_c == 1)
        {
            printf ", "
        }
    }
    else
    {
        if(ended == 0)
        {
            printf "\n"
            ended = 1
        }
    }


    if(is_word == 1)
    {
        printf "%d words", count_w
        ++printed
        print_w = 1
    }

    if(num_args > printed)
    {
        if(print_w == 1)
        {
            printf ", "
        }
    }
    else
    {
        if(ended == 0)
        {
            printf "\n"
            ended = 1
        }
    }


    if(is_line == 1)
    {
        printf "%d lines", count_l
        ++printed
        print_l = 1
    }

    if(num_args > printed)
    {
        if(print_l == 1)
        {
            printf ", "
        }
    }
    else
    {
        if(ended == 0)
        {
            printf "\n"
            ended = 1
        }
    }


    if(is_para == 1)
    {
        printf "%d paragraphs", count_p
        ++printed
        print_p = 1
    }

    if(num_args > printed)
    {
        if(print_p == 1)
        {
            printf ", "
        }
    }
    else
    {
        if(ended == 0)
        {
            printf "\n"
            ended = 1
        }
    }

}'