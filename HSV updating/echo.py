import socket

s = socket.socket()
s.bind(('', 5990))
s.listen(1)
conn, adrs = s.accept()
print "Connected to-"
print adrs


HSV_array = []

HSV_array.append(conn.recv(1024))

print HSV_array
raw_input("staaaap")
