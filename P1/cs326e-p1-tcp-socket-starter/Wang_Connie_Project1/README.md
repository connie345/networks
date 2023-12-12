
# Assignment 1: Socket & Multithreaded Programming
![enter image description here](https://us.123rf.com/450wm/bignai/bignai1807/bignai180700125/104198009-hand-plugs-internet-cable-into-wifi-extender-device-is-in-electrical-socket-on-the-wall.jpg)
## Socket Programming

As discussed in lecture, socket programming is the standard way to write
programs that communicate over a network. While originally developed for Unix
computers programmed in C, the socket abstraction is general and not tied to
any specific operating system or programming language. This allows programmers
to use socket to write correct network programs in many contexts.

This part of the assignment will give you experience with basic socket
programming. You will write a pair of TCP client and server programs for
sending and receiving text messages over the Internet.

The client and server programs in both languages should meet the following
specifications. Be sure to read these meticulously before and after programming
to make sure your implementation fulfills them:

### Server specification
* Each server program should listen on a socket, wait for a client to connect,
  receive a message from the client, print the message to stdout, and then wait
  for the next client indefinitely.
* Each server should take one command-line argument: the port number to listen
  on for client connections.
* Each server should accept and process client communications in an infinite
  loop, allowing multiple clients to send messages to the same server. The
  server should only exit in response to an external signal (e.g. SIGINT from
  pressing `ctrl-c`).
* Each server should maintain a short (10) client queue and handle multiple
  client connection attempts currently via **multithreaded programming**.

### Client specification
* Each client program should contact a server, read a message from stdin, send
  the message, and exit.
* Each client should read and send the message **exactly** as it appears in stdin
  until reaching an EOF (end-of-file).
* Each client should take two command-line arguments: the IP address of the
  server and the port number of the server.
* Each client must be able to handle arbitrarily large messages by iteratively
  reading and sending chunks of the message, **rather than reading the whole message into memory first**.
* Each client should handle partial sends (when a socket only transmits part of
  the data given in the last `send` call) by attempting to re-send the rest of
  the data until it has all been sent.

### Getting started

### Python

The documentation for Python socket programming is located here:
https://docs.python.org/3/library/socket.html. The first few paragraphs at the
top, the [section on socket objects](https://docs.python.org/3/library/socket.html#socket-objects) and the [first example](https://docs.python.org/3/library/socket.html#example) is particularly relevant. 
The documentation for Python multithreaded programming is located here: 
[what is a thread](https://www.youtube.com/watch?v=YB5I2w-8YQ4), [second example](https://www.tutorialspoint.com/python3/python_multithreading.htm) on how to use it.

The files `client-python.py` and `server-python.py` contain the scaffolding
code. You will need to add socket and multithreaded programming code. 
The Python socket functions will automatically raise Exceptions with helpful
error messages. No additional error handling is required.


### Testing

The server should be run as `python3 -u server-python.py [port] > output.txt`
(DON'T forget the -u argument to force the stdout and stderr streams to be unbuffered).
The client should be run as `python3 client-python.py [server IP] [server port]
< input.txt`.

You should test your implementations by attempting to send messages from your
clients to your servers. The server can be run in the background (append a `&`
to the command) or in a separate SSH window. You should use `127.0.0.1` as the
server IP and a high server port number between 10000 and 60000. If you get the error 
`OSError: [Errno 98] Address already in use`, you can run command `pkill -9 python3` to
kill the process that occupies the port. And, if you get a permissions error, 
run `chmod a+wrx server-python.py client-python.py` to give the script execute privileges.

You should compare the two files using `diff in.txt out.txt`. If nothing returns that means 
your output file matches your input file. In addition, you can use the provided Robots_of_the_World!_Arise!.txt
to test your program.


### Submission and grading

Submit the assignment by uploading your modified client and server files to **Canvas**.

We will grade your assignments by running it on the CS lab machine.
Double check the specifications above and perform your own tests before
submitting.

Code that does not compile is graded harshly; if you want partial credits,
*make sure your file compiles!*
