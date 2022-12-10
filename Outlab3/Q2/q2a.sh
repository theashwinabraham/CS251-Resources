#! /bin/bash

FINAL=${2-"final.csv"}

awk 'BEGIN {
    FS = ","
    months["01"] = "January"
    months["02"] = "February"
    months["03"] = "March"
    months["04"] = "April"
    months["05"] = "May"
    months["06"] = "June"
    months["07"] = "July"
    months["08"] = "August"
    months["09"] = "September"
    months["10"] = "October"
    months["11"] = "November"
    months["12"] = "December"
}

{
    if(NR == 1)
    {
        printf "%s,%s,Date,Time\n", $1, $2
    }
    else
    {
        printf "%s,%s,", $1, $2
        split($3, x, "_")
        split(x[1], y, "/")
        split(x[2], z, ":")
        tz = "AM"
        if(z[1] == 0)
        {
            z[1] = 12
        }
        else if(z[1] >= 12)
        {
            tz = "PM"
            if(z[1] > 12) z[1] -= 12;
        }
        printf "%s %s %s,%s:%s%s\n", y[3], months[y[2]], y[1], z[1], z[2], tz
    }
}' $1 > $FINAL