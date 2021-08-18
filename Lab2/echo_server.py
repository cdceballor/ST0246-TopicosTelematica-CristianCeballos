import socket	# Import socket module
import sys
from _thread import *
from http.server import BaseHTTPRequestHandler, HTTPServer

s = socket.socket() # Create a socket object

#host = socket.gethostname()   # Get local machine name
#port = 65432#int(sys.argv[1])
#s.bind(("localhost", 8080))  # Bind to the port
#s.listen(5)  # Now wait for client connection.

print("Server is up and running")

class HandlerConection(BaseHTTPRequestHandler):
     def _set_response(self):
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()

     def do_GET(self):
          #print("GET request,\nPath: {} \nHeaders: {} \n".format(self.path, self.headers))
          c, addr = s.accept()
          #options = str(self.path).split
          connection(c)
          self._set_response()
          self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

     def do_POST(self):
          content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
          post_data = self.rfile.read(content_length) # <--- Gets the data itself
          print("POST request,\nPath: {}\nHeaders:{}\nBody:\n%s\n",
          str(self.path), str(self.headers), post_data.decode('utf-8'))

          self._set_response()
          self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def connection(c):
          while True:
               try:
                    #equation = c.get('localhost:8080')
                    equation=c.recv(1024).decode()
                    print(equation)
                    if equation == "Q" or equation == "q" or equation == "Quit" or equation == "quit" or equation == "quit()":
                         c.send("Quit".encode())
                         break
                    else:
                         print("You gave me the equation:", equation)
                         result = eval(equation)
                         c.send(str(result).encode())
               except (ZeroDivisionError):
                    c.send("ZeroDiv".encode())
               except (ArithmeticError):
                    c.send("MathError".encode())
               except (SyntaxError):
                    c.send("SyntaxError".encode())
               except (NameError):
                    c.send("NameError".encode())
          c.close() 			# Close the connection.

try:
     server = HTTPServer(('localhost', 8080), HandlerConection)
     print("Starting server, use <Ctrl-C> to stop")
     server.serve_forever()
except Exception as error:
     print("Server error")
     print(error)
# while True:
#      c, addr = s.accept() # Establish connection with client.
#      print('Got connection from', addr)
#      start_new_thread(connection, (c, ))
