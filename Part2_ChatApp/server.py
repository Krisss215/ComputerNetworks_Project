import socket
import threading


HOST = '127.0.0.1'
PORT = 5555
clients = {}


def handle_client(client_socket):
    username = None
    try:

        username = client_socket.recv(1024).decode('utf-8')
        clients[username] = client_socket
        print(f"[NEW CONNECTION] {username} connected.")
        client_socket.send(f"Welcome {username}! To chat, type: TARGET:MESSAGE".encode('utf-8'))

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break


            if ":" in message:
                target_name, msg_content = message.split(":", 1)
                if target_name in clients:
                    target_socket = clients[target_name]
                    # Send format: "Sender: Message"
                    target_socket.send(f"{username}: {msg_content}".encode('utf-8'))
                else:
                    client_socket.send(f"User {target_name} not found.".encode('utf-8'))
            else:
                client_socket.send("Error: Use format 'TARGET:MESSAGE'".encode('utf-8'))

    except Exception as e:
        print(f"[ERROR] {username}: {e}")
    finally:
        if username and username in clients:
            del clients[username]
        client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[STARTING] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


if __name__ == "__main__":
    start_server()