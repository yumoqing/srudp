from srudp import SecureReliableSocket
from time import sleep, time
import sys

sock = SecureReliableSocket()
sock.connect((sys.argv[1], int(sys.argv[2])))
  
while not sock.is_closed:
	sock.sendall(b'hello ' + str(time()).encode())
	sleep(3)
print("closed", sock)
