import socket
import sys

ip = '192.168.178.7'
port = 6666

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (ip, port)
print('connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address)

try:

    # Send data
    message = '0;60;60;10'
    print('sending "%s"' % message, file=sys.stderr)
    sock.sendto(message.encode(), (ip, port))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)
        print('received "%s"' % data, file=sys.stderr)

finally:
    print('closing socket', file=sys.stderr)
    sock.close()
