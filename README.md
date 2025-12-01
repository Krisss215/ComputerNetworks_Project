# ComputerNetworks_Project
Part 1 — HTTP Packet Analysis
Goal:
Analyze raw HTTP packet data from a CSV file and extract meaningful information about the communication.
Input: group01_http_input.csv contains HTTP request/response packet data.
Features
✔ Parse and analyze HTTP packets
✔ Identify packet types (GET, POST, RESPONSE, etc.)
✔ Extract headers and payload information
✔ Compute useful statistics (message counts, IPs, content types, and more)
✔ Print formatted summary of all packet data

Part 2 — Chat Application (Client/Server)
Goal:
Implement a basic TCP chat system using Python sockets.
Components:
server.py
Handles multiple clients
Assigns clients unique addresses
Receives and broadcasts messages
Manages connection lifecycle

client.py
Connects to the server
Sends messages
Receives broadcast messages
Simple terminal chat interface

Captured Example
See: captured messages.png
