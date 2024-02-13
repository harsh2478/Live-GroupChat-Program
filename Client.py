import socket
import sys
import select

# Same step that we take in server.py
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print ("Correct usage: script, IP address, port number")
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
client_socket.connect((IP_address, Port))

def main():
    while True:
        sockets = [sys.stdin, client_socket]
      
# The select.select() function is useful for programs that need to monitor multiple input and output streams without blocking.
# The select.select() function blocks until at least one of the objects in the readable, writable, or exceptional becomes ready for I/O. 
        readable, writable, exceptional = select.select(sockets, [], [])

        for socket in readable:
            if socket == client_socket:
                print()
                message = socket.recv(2048)
                print(message)
                print()

            else:
                message = sys.stdin.readline()
                client_socket.send(message.encode('utf-8'))
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()

    client_socket.close()

if __name__ == '__main__':
    main()
