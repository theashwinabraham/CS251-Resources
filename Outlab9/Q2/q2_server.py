# AUTHOR: ASHWIN ABRAHAM

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import magic

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8080), logRequests=False, requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    # server.register_function(pow)

    # Register a function under a different name
    # def adder_function(x, y):
    #     return x + y
    # server.register_function(adder_function, 'add')

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').
    # class MyFuncs:
    #     def mul(self, x, y):
    #         return x * y

    # server.register_instance(MyFuncs())

    server.register_function(magic.getMagicNumber, 'getMagicNumber')

    quit = 0
    def kill():
        global quit
        quit = 1
        return 1
    
    server.register_function(kill)

    # Run the server's main loop
    while not quit:
        server.handle_request()
