import xmlrpc.client
import sys

if len(sys.argv) != 2:
    print(f'Usage python3 {sys.argv[0]} <float number>')
    exit(-1)

s = xmlrpc.client.ServerProxy('http://localhost:8080')
# print(s.pow(2,3))  # Returns 2**3 = 8
# print(s.add(2,3))  # Returns 5
# print(s.mul(5,2))  # Returns 5*2 = 10

# # Print list of available methods
# print(s.system.listMethods())

print(s.getMagicNumber(float(sys.argv[1])))

s.kill()