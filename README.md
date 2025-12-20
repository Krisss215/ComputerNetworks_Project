# ComputerNetworks_Project

## Part 1 — TCP/IP Packet Encapsulation & Analysis

### Goal
Analyze TCP/IP network traffic generated from application-layer messages
and observe the encapsulation process using Wireshark.

### Input
`group05_chat_input.csv`  
The CSV file contains simulated chat messages with the following fields:
- msg_id
- app_protocol
- src_app
- dst_app
- message
- timestamp

### Description
A Python notebook reads the CSV file row by row and sends each message
over a TCP socket to a local server running on localhost.
The generated traffic is captured using Wireshark on the loopback interface (lo0).

Although a raw packet crafting approach was initially implemented,
macOS restrictions on raw sockets require the use of standard TCP sockets.
This still allows full observation of the TCP/IP encapsulation process,
including connection establishment, data transfer, and termination.

### Features
✔ Read and parse CSV application data  
✔ Send application payload over TCP sockets  
✔ Capture traffic using Wireshark  
✔ Observe TCP 3-way handshake (SYN, SYN-ACK, ACK)  
✔ Analyze PSH, ACK packets carrying application data  

---

## Part 2 — Chat Application (Client/Server)

### Goal
Implement a multi-client TCP chat system using Python sockets
to demonstrate real-time client-server communication.

### Components

#### server.py
- Listens for incoming TCP connections
- Handles multiple clients using threads
- Maintains an in-memory dictionary of connected users
- Forwards messages between clients
- Manages connection lifecycle

#### client.py
- Connects to the server using TCP
- Sends user messages
- Receives messages asynchronously
- Terminal-based chat interface

### Network Analysis
Chat traffic between multiple clients was captured using Wireshark.
The capture shows:
- TCP connection establishment
- Data transfer using PSH, ACK packets
- Proper connection termination

---

## How to Run

### Part 1
1. Open the notebook `Group05_Part1_Notebook.ipynb`
2. Run the cells to send messages from the CSV file
3. Capture traffic in Wireshark on interface `lo0`

### Part 2
1. Run the server:
2. Run two clients in separate terminals:
3. Enter usernames and start chatting

---

## Files
- `group05_chat_input.csv` — application input data
- `Group05_Part1_Notebook.ipynb` — packet generation and analysis
- `chat_capture.pcapng` — Wireshark capture
- `server.py`, `client.py` — chat application
- `Report.docx` — full project report
