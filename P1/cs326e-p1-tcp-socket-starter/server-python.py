###############################################################################
# server-python.py
# Name:
# EID:
###############################################################################

import sys
import socket
import threading

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def thread(server_socket, addr):
    with server_socket:
            #print('Connected by', addr)
            while True:
                #print("recv")
                data = server_socket.recv(RECV_BUFFER_SIZE)
                print(str(data, 'utf-8'))
                if not data: 
                    break
                server_socket.sendall(data)

def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = server_port            # Arbitrary non-privileged port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
       # print("start listening....\n")
        s.listen(10)
        while(1):
            conn, addr = s.accept()
            worker_thread = threading.Thread(target=thread, args=(conn, addr)) 
            worker_thread.start()


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()
