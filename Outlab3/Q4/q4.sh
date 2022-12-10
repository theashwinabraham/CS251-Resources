#! /bin/bash

cat $1 | awk 'BEGIN {
    alph[10] = "a"
    alph[11] = "b"
    alph[12] = "c"
    alph[13] = "d"
    alph[14] = "e"
    alph[15] = "f"
    num["a"] = 10
    num["b"] = 11
    num["c"] = 12
    num["d"] = 13
    num["e"] = 14
    num["f"] = 15
    for(i = 0; i<10; i++)
    {
        num[i] = i
    }
}

{
    if(NR == 1)
    {
        test_cases = $1
    }
    else if(NR % 3 == 2)
    {
        binput = $1
        boutput = $2
    }
    else if(NR % 3 == 0)
    {
        num1 = 0
        for(i = 1; i<=NF; i++)
        {
            num1 *= binput
            num1 += num[$i]
        }
    }
    else
    {
        num2 = 0
        for(i = 1; i<=NF; i++)
        {
            num2 *= binput
            num2 += num[$i]
        }
        noutput = num1 + num2
        if(noutput == 0)
        {
            print 0
        }
        else
        {
            num_trail = 0
            while(noutput % boutput == 0)
            {
                num_trail++
                noutput = int(noutput/boutput)
            }
            nrev = 0
            while(noutput > 0)
            {
                nrev *= boutput
                nrev += noutput % boutput
                noutput = int(noutput/boutput)
            }
            while(nrev > 0)
            {
                if(nrev % boutput > 9)
                {
                    printf alph[nrev % boutput]
                }
                else
                {
                    printf nrev % boutput
                }
                
                if(int(nrev / boutput) == 0 && num_trail == 0)
                {
                    printf "\n"
                }
                else
                {
                    printf " "
                }
                nrev = int(nrev/boutput)
            }
            for(i = 0; i<num_trail; ++i)
            {
                printf 0
                if(i == num_trail - 1)
                {
                    printf "\n"
                }
                else
                {
                    printf " "
                }
            }
        }
    }
}' > $2