import sys, os

x = int(os.system(f'ping -c 5 {sys.argv[1]} > /dev/null'))
if x == 0:
    print('YES')
else:
    print('NO')