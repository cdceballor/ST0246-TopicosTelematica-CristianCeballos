import socket		 	 # Import socket module
import sys
import ipaddress
import requests
import http.client

s = socket.socket() 	  		 # Create a socket object

try:
    #54.236.45.39
    # host = socket.gethostname()  # Reading IP Address
    # port = 65432 # Reading port number
    # s.connect(("localhost", 8080))  # Connecting to server
    # print("The IP address of the server is:", host)
    # print("The port number of the server is:", port)

    while(True):
        equ=input("Please give me your equation (Ex: 2+2) or Q to quit: ")
        s = requests.post("http://localhost:8080", equ)
        print(s)
        #s.send(equ.encode())
        #result = s.recv(1024).decode()
        result = s
        if result == "Quit":
            print("Closing client connection, goodbye")
            break
        elif result == "ZeroDiv":
            print("You can't divide by 0, try again")
        elif result == "MathError":
            print("There is an error with your math, try again")
        elif result == "SyntaxError":
            print("There is a syntax error, please try again")
        elif result == "NameError":
            print("You did not enter an equation, try again")
        else:
            print("The answer is:", result)
            
    if(result != ""):
        connection = http.client.HTTPConnection('localhost', 8080)
        connection.request("GET", '/' + result)
        response = connection.getresponse()
        print("Status: {} and reason: {}".format(response.status, response.reason))
        connection.close()

except (IndexError, ValueError):
    print("You did not specify an IP address and port number")