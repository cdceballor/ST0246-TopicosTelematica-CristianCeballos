import socket		 	 # Import socket module
import sys
import ipaddress
import requests
import http.client
import const

PRIVATEHOSTSERVER = const.SERVERADDRESS
PUBLICHOSTCLIENT = const.CLIENTADDRESS
PUBLICHOSTCLIENTWITHPORT = const.PUBLICHOSTCLIENTWITHPORT
PORT = const.PORT

s = socket.socket() 	  		 # Create a socket object

try:

    while(True):
        equ=input("Please give me your equation (Ex: 2+2) or Q to quit:")
        #s = requests.post("http://localhost:8080", equ)
        #s = requests.post(PUBLICHOSTCLIENTWITHPORT, equ)
        s = requests.post("http://172.31.54.170:8080", equ)
        #s= requests.post("http://100.25.196.132:8080", equ)   
        #s = requests.post("http://44.197.229.178:8080", equ)
        #s = requests.post("http://172.31.2.156:8080", equ)
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
        #connection = http.client.HTTPConnection(PUBLICHOSTCLIENT, PORT)
        #connection = http.client.HTTPConnection("http://172.31.54.170", PORT)
        #connection = http.client.HTTPConnection("http://100.25.196.132", PORT)
        #connection = http.client.HTTPConnection("http://44.197.229.178", PORT)
        #connection = http.client.HTTPConnection("http://172.31.2.156", PORT)
        connection = http.client.HTTPConnection("http://localhost", PORT)
        connection.request("GET", '/' + result)
        response = connection.getresponse()
        print("Status: {} and reason: {}".format(response.status, response.reason))
        connection.close()

except (IndexError, ValueError):
    print("You did not specify an IP address and port number")