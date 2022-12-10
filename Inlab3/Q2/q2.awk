# AUTHOR: ASHWIN ABRAHAM

{
    base = 8 + 2*(NR%3);
    num = 0;
    for(i=1; i<=NF; i++)
    {
        num = num*base;
        if($i == "a")
        {
            num += 10;
        }
        else if($i == "b")
        {
            num += 11;
        }
        else
        {
            num += $i;
        }
    }
    print num;
}
