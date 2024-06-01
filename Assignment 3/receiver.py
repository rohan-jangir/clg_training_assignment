import socket

def receive_file(host, port):
    with socket.socket() as s:
        s.bind((host, port))
        s.listen()
        conn, _ = s.accept()

        with conn:
            filename = "received_file.txt"
            with open(filename, "wb") as file:
                file_data = conn.recv(1024)
                while file_data:
                    file.write(file_data)
                    file_data = conn.recv(1024)

        print(f"File received: {filename}")

receiver_host = "localhost"  # Replace with receiver's IP address if not on the same machine
receiver_port = 12345        # Make sure the receiver listens on this port
receive_file(receiver_host, receiver_port)
