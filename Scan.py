import socket
import pyfiglet
import sys
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCAN")
print(ascii_banner)

HostIP = input(str("Host IP:"))

#banner
print("_" * 50)
print('Scanning Host:' + HostIP)
print( "Scanning started at: " + str(datetime.now()))
print( "_" * 50)

#scanning

try:
    print(f"Scanning Host: {HostIP}")
    for port in range(1,65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((HostIP,port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

except  KeyboardInterrupt:
        print("\n Exiting :(")
        sys.exit()

