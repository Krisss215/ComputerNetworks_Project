import socket
import threading
import sys

# Configuration
HOST = '127.0.0.1'
PORT = 55556  # <--- CHANGED PORT to match Server


def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            if not msg: break
            print(f"\n{msg}\n> ", end="")
        except:
            print("Disconnected.")
            sock.close()
            sys.exit()


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except:
        print("Could not connect. Is the server running?")
        return

    # Login Logic
    try:
        msg = client.recv(1024).decode('utf-8')
        if msg == "ENTER_NAME":
            client.send(input("Enter Username: ").encode('utf-8'))

        msg = client.recv(1024).decode('utf-8')
        if msg == "WHO_TO_CONNECT":
            client.send(input("Chat with who?: ").encode('utf-8'))

        print(client.recv(1024).decode('utf-8'))
    except:
        return

    # Start Chatting
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        try:
            msg = input("> ")
            if msg == 'quit': break
            client.send(msg.encode('utf-8'))
        except:
            break
    client.close()


if __name__ == "__main__":
    start_client()