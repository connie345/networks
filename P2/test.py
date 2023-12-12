import socket
import os
import threading
import select
import curses
import time
from datetime import datetime
from typing import List, Tuple

BUFFER_SIZE = 2048



# ------------------------------------------ Management Console --------------------------------------------------


# ------------------------------------------ PROXY --------------------------------------------------

class HTTPRequest:
    url: str
    port: int # 80 for http and 443 for https
    https: bool
    connect_host: bytes # Parse URL for socket connection

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.parse()


    def parse(self):

        

        split_data = self.raw_data.split(b"\r\n")
        request_line = split_data[0].split(b" ")
        print(split_data)
        url = []
        self.https = False

        headers = {}
        for i in range(1, len(split_data)):
            if (split_data[i] == b""):
                break
            header = split_data[i].split(b": ")
            headers[header[0]] = header[1]

        if b"http://" in request_line[1]:
            url.append(request_line[1][7:])
        elif b":" in request_line[1]:
            self.https = True
            url = request_line[1].split(b":")
        else:
            url.append(request_line[1])

        
        print(url)
        self.url = url[0]
        self.version = request_line[2]
        self.port = 443 if self.https else 80     
        self.connect_host = self.url






def test(from_socket, to_socket):
    while True:
        try:
                 
            to_socket.sendall(from_socket.recv(BUFFER_SIZE))      
        except:
            # close sockets when done or when error
            from_socket.close()
            to_socket.close()
            return
# Create a TCP tunnel when using HTTPS
def tunnel(client_conn, http_request):
    
    server_ip = socket.gethostbyname(http_request.connect_host)
    # If not blocked, continue as normal
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.connect((server_ip ,http_request.port))
    #print(http_request.connect_host)
    #print(http_request.port)
    response = b"HTTP/1.1 200 OK\r\n\r\n"
    client_conn.sendall(response)
    t = threading.Thread(target=test, args=(client_conn,server_sock))
    t.start()
    s = threading.Thread(target=test, args=(server_sock,client_conn))
    s.start()
   

def profile_relay(client_socket, http_request):
                    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    #connect
                    server_socket.connect((http_request.connect_host, http_request.port))
                    server_socket.sendall(http_request.raw_data)
                    #send client data to server
                    server_response = b""
                    while True:
                        chunk = server_socket.recv(4096)
                        if not chunk:
                            break
                        server_response = server_response+ chunk
                    client_socket.sendall(server_response)
                    #server data to client

                    client_socket.close()
                    server_socket.close()

def handle_connection(data, client_socket):
    if data:
        http_request = HTTPRequest(data)
       
        if http_request.https:
            tunnel(client_socket, http_request)
        else:
            profile_relay(client_socket, http_request)
      

PROXY_HOST = "127.0.0.1"
PROXY_PORT = 5000

def proxy():
    # Await Connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((PROXY_HOST, PROXY_PORT))
    sock.listen(1)
 
    # Receive Requests
    while True:
        conn, addr = sock.accept()
        print("new thread")
        data = conn.recv(4096)
        thread = threading.Thread(target=handle_connection, args=(data, conn, ))
        thread.start()

def main():
    # Start Proxy
    pt = threading.Thread(target=proxy)
    pt.start()


if __name__ == "__main__":
    main()
