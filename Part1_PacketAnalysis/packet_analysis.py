import csv
import time


INPUT_FILE = 'group01_http_input.csv'


def simulate_encapsulation(row):

    msg_id = row['msg_id']
    src = row['src_app']
    dst = row['dst_app']
    message = row['message']

    print(f"\n[Packet #{msg_id}] Processing Message: '{message}'")
    print("-" * 50)


    app_layer = message
    print(f"1. [Application Layer] Data created: {app_layer}")


    tcp_header = f"[TCP | SrcPort: 12345 | DstPort: 80 | Seq: {msg_id}]"
    segment = f"{tcp_header} + {app_layer}"
    print(f"2. [Transport Layer]   Added TCP Header: {segment}")


    ip_header = f"[IP | SrcIP: 192.168.1.5 | DstIP: 10.0.0.1]"
    packet = f"{ip_header} + {segment}"
    print(f"3. [Network Layer]     Added IP Header:  {packet}")


    eth_header = f"[ETHERNET | SrcMAC: AA:BB:CC | DstMAC: DD:EE:FF]"
    frame = f"{eth_header} + {packet}"
    print(f"4. [Data Link Layer]   Added Eth Header: {frame}")
    print("-" * 50)


def main():
    try:
        print("--- STARTING PACKET ENCAPSULATION SIMULATION ---")
        with open(INPUT_FILE, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                simulate_encapsulation(row)
                time.sleep(0.5)  # Pause to simulate network delay
        print("\n--- SIMULATION COMPLETE ---")

    except FileNotFoundError:
        print(f"Error: Could not find file '{INPUT_FILE}'. Make sure it is in the same folder!")


if __name__ == "__main__":
    main()