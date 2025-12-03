import socket
import threading

# Configuration
HOST = '127.0.0.1'
PORT = 55556  # <--- CHANGED PORT to fix "Address already in use"

clients = {}


def handle_client(client_socket):
    username = ""
    try:
        # 1. Login
        client_socket.send("ENTER_NAME".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8')

        if username in clients:
            client_socket.send("NAME_TAKEN".encode('utf-8'))
            client_socket.close()
            return

        clients[username] = client_socket
        print(f"[NEW CONNECTION] {username} joined.")

        # 2. Setup Chat
        client_socket.send("WHO_TO_CONNECT".encode('utf-8'))
        target_user = client_socket.recv(1024).decode('utf-8')
        client_socket.send(f"CONNECTED: You are chatting with {target_user}".encode('utf-8'))

        # 3. Message Bridge
        while True:
            msg = client_socket.recv(1024).decode('utf-8')
            if not msg: break

            if target_user in clients:
                clients[target_user].send(f"{username}: {msg}".encode('utf-8'))
            else:
                client_socket.send(f"System: {target_user} is offline.".encode('utf-8'))
    except:
        pass
    finally:
        if username in clients: del clients[username]
        client_socket.close()
        print(f"[DISCONNECT] {username} disconnected.")


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[STARTING] Server listening on {HOST}:{PORT}")
        while True:
            client_sock, addr = server.accept()
            threading.Thread(target=handle_client, args=(client_sock,)).start()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    start_server()