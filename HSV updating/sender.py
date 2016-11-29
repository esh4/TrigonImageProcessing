import socket

sendString = raw_input("input string to send to server:")
serverIp = raw_input("servers IP adress:")
serverPort = raw_input("servers port:")
                 
s = socket.socket()
s.connect((serverIp, int(serverPort)))

print "Connected!"

s.send(sendString)

print "Message sent!"


