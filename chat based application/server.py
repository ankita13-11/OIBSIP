#Chat Based Application by Ankita Paul (server file)
import socket
import threading

# Function to handle communication with each client
def handle_client(client_socket, client_address):
    print(f"New connection: {client_address}")

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break  # Connection closed by client
            
            print(f"Message from {client_address}: {message}")
            client_socket.send(f"Server received: {message}".encode('utf-8'))
        
        except:
            print(f"Connection lost with {client_address}")
            break
    
    client_socket.close()

# Server setup
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))  # Bind to localhost and port 5555
    server.listen(5)
    print("Server is running and waiting for connections...")

    while True:
        client_socket, client_address = server.accept()  # Accept a new connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
    