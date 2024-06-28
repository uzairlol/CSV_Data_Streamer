import zmq

# Initialize ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.SUB)
# Use the internal IP address of the publisher laptop
socket.connect("tcp://192.168.1.x:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "")

# Receive and print data
print("Waiting for data...")
while True:
    message = socket.recv_string()
    print(f"Received: {message}")