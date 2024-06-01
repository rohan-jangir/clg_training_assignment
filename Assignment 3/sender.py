import socket

def send_file(filename, host, port):
    with open(filename, "rb") as file:
        file_data = file.read()

    with socket.socket() as s:
        s.connect((host, port))
        s.sendall(file_data)

filename = "hello.txt"
receiver_host = "localhost"  
receiver_port = 12345        
send_file(filename, receiver_host, receiver_port)