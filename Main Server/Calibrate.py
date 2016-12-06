import socket

class Calib:
    def __init__(self, PCport):
        self.port = PCport

    def run(self):
        global HSVvalues
        self.connect()
        func = self.getCommands()

        if func[0] == -1:
            pass
        else:



    def connect(self):
        print "-> Ready"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', self.port))
        s.listen(1)
        print 'wait for connect'
        conn, address = s.accept()
        self.conn = conn
        print address

'''
PC commands:
    [(lowThresh), (highThresh), getImage(bool), getHSVimg]
'''

    def getCommands(self, command=-1):
        PCin = self.conn.recv(1024)
        if command != -1:
            return PCin[command]
        else:
            return PCin

    def