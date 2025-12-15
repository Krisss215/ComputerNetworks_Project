import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

# --- CONFIGURATION ---
HOST = '127.0.0.1'
PORT = 55556  # UPDATED TO 55556


class ChatClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("Python Chat App (TCP)")
        master.geometry("500x600")

        # 1. Connect to Server
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((HOST, PORT))
        except ConnectionRefusedError:
            messagebox.showerror("Error", f"Could not connect to server on port {PORT}. Is it running?")
            master.destroy()
            return

        # 2. Ask for Username
        self.username = simpledialog.askstring("Username", "Choose a Username:", parent=master)
        if not self.username:
            self.sock.close()
            master.destroy()
            return

        self.sock.send(self.username.encode('utf-8'))

        # --- GUI LAYOUT ---
        # Chat Display Area
        self.display_area = scrolledtext.ScrolledText(master, state='disabled', wrap='word', font=("Arial", 12))
        self.display_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Bottom Frame for Input
        bottom_frame = tk.Frame(master)
        bottom_frame.pack(padx=10, pady=10, fill=tk.X)

        # Message Entry Box
        self.msg_entry = tk.Entry(bottom_frame, font=("Arial", 12))
        self.msg_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.msg_entry.bind("<Return>", self.send_message)

        # Send Button
        send_btn = tk.Button(bottom_frame, text="Send", command=self.send_message, bg="#4CAF50", fg="white",
                             font=("Arial", 10, "bold"))
        send_btn.pack(side=tk.RIGHT)

        # Helper Label
        info_label = tk.Label(master, text="Format: TARGET:MESSAGE (e.g., Bob:Hello)", fg="grey")
        info_label.pack(pady=(0, 10))

        # 3. Start Listening Thread
        self.running = True
        threading.Thread(target=self.receive_loop, daemon=True).start()

    def receive_loop(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if not message:
                    break
                self.append_message(message)
            except:
                break
        self.sock.close()

    def send_message(self, event=None):
        msg = self.msg_entry.get()
        if msg:
            try:
                self.sock.send(msg.encode('utf-8'))
                self.append_message(f"Me: {msg}")
                self.msg_entry.delete(0, tk.END)
            except:
                messagebox.showerror("Error", "Connection lost.")
                self.master.destroy()

    def append_message(self, text):
        self.display_area.config(state='normal')
        self.display_area.insert(tk.END, text + "\n")
        self.display_area.see(tk.END)
        self.display_area.config(state='disabled')

    def on_closing(self):
        self.running = False
        self.sock.close()
        self.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    gui = ChatClientGUI(root)
    root.protocol("WM_DELETE_WINDOW", gui.on_closing)
    root.mainloop()