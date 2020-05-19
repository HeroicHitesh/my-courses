## Client-Server Model ##
A **server** is a centralized program that communicates over a network (such as the Internet) to serve clients.

And a **client** is a program (like the web browser on your computer) that can request data from a server.

**Servers, Clients, Hosts**
- In a Client-Server Model, a server serves many clients.
- Servers and clients are programs that run on hosts.
- Hosts are computers connected over a network (like the internet!).

**Requests and Responses**
- A client sends a request to the server
- The server's job is to fulfill the request with a response it sends back to the client.
- Requests and responses are served via a communication protocol, which sets up the expectations and rules for how the communication occurs between servers and clients.

**Relational Database Clients**
- A database client is any program that sends requests to a database
- In some cases, the database client is a web server! When your browser makes a request, the web server acts as a server (fulfilling that request), but when the web server requests data from the database, it is acting as a client to that database—and the database is the server (because it is fulfilling the request).

**QUESTION 1 OF 6**

Let's review the basic vocabulary we've covered. See if you can match each term with the correct description.
DESCRIPTION | TERM
------------|------
A common language that the client and server use to communicate with each other. | Communication Protocol
A centralized system that communicates over a network to serve many clients. | Server
A computer connected to the network (which could be running either a client or server program) . | Host
A program that can request data from a server. | Client

**QUESTION 2 OF 6**

A client is responsible for sending a...
- [ ] Request to the client
- [ ] Response to the client
- [x] Request to the server
- [ ] Response to the server

**QUESTION 3 OF 6**

A server is responsible for sending a...
- [ ] Request to another server
- [ ] Request to the client
- [x] Response fulfilling a client's request
- [ ] Response from another server

**QUESTION 4 OF 6**

To a database server, a web server is a....
- [x] Client
- [ ] Server
- [ ] Both a Client and a Server

**QUESTION 5 OF 6**

To a web client, a web server is a...
- [ ] Client
- [x] Server
- [ ] Both a Client and a Server

**QUESTION 6 OF 6**

See if you can fill in the blanks in the sentences below.
SENTENCE | CLIENT / SERVER / HOST
---------|-----------------------
The ____ sends a request to the ____. | client, server
The ____ sends a response to the ____. | server, client
The client is run on a ____. | host
The server is run on a ____. | host
The database ____ treats the web ____ as a client. | server, server
