# IMPLEMENTED BY: ASHWIN ABRAHAM

# Running your solution - You can run this script in console with the command given in the next line
# python q2.py 10
# Here 10 is the input provided by the user. Hence the output should be the list of prime numbers less than or equal to 10. Your console output shpuld be:
# List of primes = [2,3,5,7]

########################################## Script starts here ########################################
import sys
import functools
import matplotlib.pyplot as plt
# This python module can be used for getting the input provided by user
  
def get_primes(num):
   # Should take an integer as input and return a list of primes less than or equal to the given input
   # l = map(lambda n: (n, True), range(2, num+1))
   # l = list(range(2, 11))
   # p = list(map(lambda t : set(filter(lambda s : s == t or s % t != 0, l)), l))
   # return functools.reduce(set.intersection, p)
   l =  sorted(list(functools.reduce(set.intersection, map(lambda t : set(filter(lambda s : s == t or s % t != 0, range(2, num+1))), range(2, num+1)))))
   print(l)
   x = range(1, len(l)+1)
   plt.scatter(x, l)
   plt.title(f'Prime numbers till {num}')
   plt.show()
# the variable num should be declared before the main() function as a global variable

if __name__ == '__main__':
    # Edit this part of the code in order to pass the argument to get_primes() function
    # num is the argument you got from command line using argparse module
    get_primes(int(sys.argv[1]))