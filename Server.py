import socket
import threading 
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print()
print("\t\t\t\tYOUR GROUPCHAT STARTED")
print("\t\t\t\tWAIT FOR MEMBERS TO JOIN.....")

# sys.argv takes the argument on the runtime and store in a list, placing the script name at the fist position
if len(sys.argv) != 3: 
  #If the user doesn't enter the 3 command argument, then it gives this error to use correct syntax with order
    print ("Correct usage: script, IP address, port number")  
    exit() 

IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 

#Binding the  IP address and port number to create the socket
server.bind((IP_address, Port)) 

#Setting the connection for maximum 50 clients
server.listen(50)

#An empty list for storing the connections of coming clients
clients = []

def handling_client(con, addr):
    con.send(b"Welcome to Harsh Server chatgroup!")
    while True:
        try:
            message = con.recv(2048)
            data = message.decode('utf-8')
            if data:
                print("<< ", addr[0] , " >> " , data)
              #Below we have to send the message to all as it is group chat and it is server duty to send the message to all
                message_to_send = "<" + addr[0] + "> " + data
                for target in clients:
                  # Exclude the client who sent the message
                    if target != con:  
                        try:
                            target.send(message_to_send.encode())
                        except:
                            target.close()
                            rem(target)
        except:
            continue

# Function to remove the clients from list 
def rem(connection):
    if connection in clients:
        clients.remove(connection)

def main():
    while True:
        con, addr = server.accept()
        clients.append(con)
        print("MEMBER ", addr[0], " ENTERED IN THE CHAT ")
        print()
      # Starting the thread for this program
        client_handler = threading.Thread(target=handling_client, args=(con, addr,))
        client_handler.start()

if __name__ == '__main__':
    main()
