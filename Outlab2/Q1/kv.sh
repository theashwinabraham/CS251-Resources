#! /bin/bash
# AUTHOR: ASHWIN ABRAHAM

if [ "$1" = "storeInfo" ]
then
    printf "$2_$(date +%d/%m/%y-%T) $3\n" >> store.txt
elif [ "$1" = "displayInfo" ]
then
    echo "Name OrderID"
    cat store.txt
elif [ "$1" = "getOrderID" ]
then
    function my_read()
    {
        var=0
        while read -r line
        do
            echo "$line"
            let "var += 1"
        done
        printf "$1 ordered $var times\n"
    }
    echo "Order ID's found are:"
    cat store.txt | grep -Ex "$2_([0-9]{2}\/){2}[0-9]{2}-([0-9]{2}:){2}[0-9]{2} [0-9]{1,7}" | tr " " "\n" | grep -Ex "[0-9]{1,7}" | my_read $2
fi