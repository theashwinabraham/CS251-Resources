BEGIN {
}

{
    split($0, line)
    for(i in line)
        freq[line[i]] = 1 + freq[line[i]]
}

END {
    for(i in freq)
        print i, freq[i]
}