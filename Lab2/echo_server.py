import socket	# Import socket module
import sys
from _thread import *
from http.server import BaseHTTPRequestHandler, HTTPServer

s = socket.socket() # Create a socket object

print("Server is up and running")

class HandlerConection(BaseHTTPRequestHandler):
     def _set_response(self):
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()

     def do_GET(self):
          c, addr = s.accept()
          connection(c)
          self._set_response()
          self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

     def do_POST(self):
          content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
          post_data = self.rfile.read(content_length) # <--- Gets the data itself
          print(post_data.decode('utf-8'))
          post_data = str(post_data.decode('utf-8')).strip()
          print(post_data)
          if(len(post_data.split('+')) > 1):
            result= int(post_data.split('+')[0]) + int(post_data.split('+')[1])

          if(len(post_data.split('-')) > 1):
            result=int(post_data.split('-')[0]) - int(post_data.split('-')[1])

          if(len(post_data.split('*')) > 1):
            result=int(post_data.split('*')[0]) * int(post_data.split('*')[1])

          if(len(post_data.split('/')) > 1):
            result=int(post_data.split('/')[0]) / int(post_data.split('/')[1])

          print(result)
          self._set_response()
          self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def connection(c):
          while True:
               try:
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
     # Puerto : 8008
     # IP : privada intancia que va a ser el server - 172.31.2.156
     #server = HTTPServer(('localhost', 8080), HandlerConection)
     server = HTTPServer(('172.31.2.156', 8080), HandlerConection)
     print("Starting server, use <Ctrl-C> to stop")
     server.serve_forever()
except Exception as error:
     print("Server error")
     print(error)