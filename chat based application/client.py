#Chat Based Application by Ankita Paul (client file)
import socket

# Client setup
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))  # Connect to server at localhost and port 5555

    print("Connected to the server.")
    
    while True:
        message = input("You: ")
        
        if message.lower() == 'quit':
            print("Connection closed.")
            client.close()
            break
        
        client.send(message.encode('utf-8'))  # Send message to server
        
        # Wait for and receive a response from the server
        response = client.recv(1024).decode('utf-8')
        print(f"Server: {response}")

if __name__ == "__main__":
    start_client()
    