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

receiver_host = "localhost"  
receiver_port = 12345        
receive_file(receiver_host, receiver_port)
