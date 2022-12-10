# 210050023-git
| Roll Number | Name |
| ----------- | ----------- |
| 210050023 | Ashwin Abraham |

This repository was mainly created as a part of our Software Systems Lab Course (CS 251) to give us experience in using ```git```.
We initialized this repository with a README file and then added the files ```hashing.hpp```, ```hashing.cpp``` and ```main.cpp```.
We also wrote a Shell Script ```test.sh``` that compiled and executed these files.

We then implemented a hash function that hashed a string by taking the sum of all ASCII values of the characters of string modulo a prime.

That is, 

$hash(s) = (\sum_{i} s_{i}) \mod m$

where m is a prime.


We then created a new branch of the repo and wrote a different implementation of the Hash Function, using Polynomial Accumulation.

That is, 

$hash(s) = (\sum_{i} s_{i}p^{i}) \mod m$

where m and p are primes.


We then created a new branch of the repo and wrote a different implementation of the Hash Function, using Polynomial Accumulation.
We then modified the main branch by changing the signature of our hash function.
We then merged the two branches and fixed the merge conflicts that occured.

The hash function that we have written may be very useful while making **Hash Tables**, which are a set of key-value pairs that have highly efficient *Insertion*, *Deletion* and *Retrieval* operations.

## Usage Instructions
To compile and execute this file, simply execute the Shell Script provided (```test.sh```) and provide the string you wish to hash as a command line argument.
For example,
```
./test.sh welcometoSSL
```

The file ```test.sh``` checks if you have the *GNU C++ Compiler* (```g++```) added to your path, and, if so, compiles ```main.cpp``` with it and links it to ```hashing.cpp``` and executes the resulting executable (```a.out```), providing the command line arguments that you have provided as it's command line arguments.

The contents of ```test.sh``` are:
```
GCC=$(which g++)

if [ "$GCC" == "" ]; then
    echo "Please install GCC and add it to PATH"
else
    $GCC -c hashing.cpp -o hashing.o
    $GCC hashing.o main.cpp -o a.out
    ./a.out $1
fi
```

## Solution to Question 1 (Bash)
In question 1, we had to write two aliases in our ```~/.bashrc``` file:
- ```sizeOfFiles```: This gets the space usage of all the child files and directories of the current directory and displays it on the terminal
- ```numberOfFiles```: This returns the count of all the child files and directories of the current directory

These aliases were written using the ```du``` (**Disk Usage**) command, that displays the space usage of files and directories and the ```wc``` (**Word Count**) command which returns the number of characters, words and lines in a stream.

The exact form of the aliases are:
```
alias sizeOfFiles="du -ah"
alias numberOfFiles="du -ah | wc -l"
```
The ```-ah``` flag in ```du``` tells ```du``` to display all files (including hidden files) in a human readable format, and the ```-l``` flag in ```wc``` tells it to display the number of lines.

These two lines were added to the end of my ```~/.bashrc``` file.

## References
Some references that I used were:
- [Geeks for Geeks](https://www.geeksforgeeks.org/du-command-linux-examples/)
- [Ryan's Tutorials on Bash](https://ryanstutorials.net/bash-scripting-tutorial/bash-arithmetic.php)
- [W3 Schools tutorial on Git](https://www.w3schools.com/git/)
- [Atlassian tutorial on Git](https://www.atlassian.com/git/tutorials)
- [Unix and Linux Stack Exchange](https://unix.stackexchange.com/)
- [Stack Overflow](https://stackoverflow.com/)