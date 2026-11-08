# udp-lab
# UDP Reliable Messaging

A client/server program in Python using UDP sockets.
Since UDP is unreliable, I added ACK, timeout and retransmission.

## Features
- ACK for every message
- Retransmission after 1 second timeout (max 5 tries)
- Commands: upper, reverse, count
- Simulated packet loss (30%) on the server

## How to run
1. python UDPServer.py
2. In another terminal: python UDPClient.py
