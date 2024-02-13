# Live-GroupChat-Program

Project Title: Live Chat Program

Objective: The objective of this project is to create a real-time group chat application where multiple users can connect to a central server and communicate with each other.


Features:

  Real-Time Communication: Users can send and receive messages in real-time.

  Group Chat: The application supports group chat functionality where messages are broadcasted to all connected users.

  Server-Client Architecture: The project follows a client-server architecture, where the server facilitates communication between clients.

  Welcome Message: When a client connects to the server, they receive a welcome message.

  Error Handling: The server and client code include error handling to ensure smooth operation and graceful termination in case of errors.

  Multithreading: The server utilizes multithreading to handle multiple client connections simultaneously, ensuring that one client's actions do not block others.


Components:

  Server: The server component creates a socket and listens for incoming connections from clients. It maintains a list of connected clients and broadcasts messages received from one client to all other clients.

  Client: The client component connects to the server, sends messages to the server, and receives messages from other clients through the server.


Technologies Used:

  Python: The project is implemented using Python programming language.

  Socket Programming: Socket programming is used for network communication between the server and clients.

  Threading: Threading is used to handle multiple client connections concurrently on the server side.


Usage:

  Server Setup: The server is started with the specified IP address and port number.

  Client Connection: Clients connect to the server by specifying the server's IP address and port number.

  Chatting: Once connected, clients can send messages to the server, which are then broadcasted to all other connected clients.
