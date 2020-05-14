from srudp import SecureReliableSocket
from time import time
import sys

sock = SecureReliableSocket()
sock.connect((sys.argv[1], 12345))
 
while not sock.is_closed:
    data = sock.recv(1024)
    if not data:
        break
    print(time(), data)
print("closed", sock)
