import socket
import threading

# Client Configuration
HOST = '127.0.0.1'
PORT = 5555

def receive_messages(client_socket):
    """Listens for incoming messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            # Print the new message and re-print the prompt so it looks clean
            print(f"\n{message}\nYour message: ", end="")
        except:
            print("[ERROR] Connection lost.")
            client_socket.close()
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect to server. Is it running?")
        return

    # 1. Send Username
    username = input("Enter your username: ")
    client.send(username.encode('utf-8'))

    # 2. Start a thread to listen for incoming messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    # 3. Main loop to send messages
    print("Format to chat -> TARGET_NAME:MESSAGE (e.g., alice:hello)")
    while True:
        msg = input("Your message: ")
        if msg.lower() == 'exit':
            break
        client.send(msg.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    start_client()