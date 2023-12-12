###############################################################################
# client-python.py
# Name:
# EID:
###############################################################################

import sys
import socket

SEND_BUFFER_SIZE = 2048

def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    SERVER_HOST = server_ip    # 128.83.130.135
    SERVER_PORT = server_port             # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT)) # waits for server accept
        while (1):
            try:
                f = input()
                res = bytes(f, 'utf-8')
                client_socket.sendall(res)
                data = client_socket.recv(SEND_BUFFER_SIZE)
                print('Received', repr(data))   
            except EOFError as e:
                break

def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()
