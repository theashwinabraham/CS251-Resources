BEGIN {
}

{
    split($0, line)
    for(i in line)
        freq[line[i]] = 1 + freq[line[i]]
}

END {
    sum = 0
    for(i in freq)
        sum += 1
    print sum
}