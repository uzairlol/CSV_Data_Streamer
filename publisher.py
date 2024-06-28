import zmq
import pandas as pd
import time

# Path to the CSV file
csv_file_path = 'dataset.csv'

# Load CSV data
df = pd.read_csv(csv_file_path)

# Initialize ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.PUB)
# Binding to the internal IP address of the publisher laptop
socket.bind("tcp://192.168.1.x:5555")

# Publish CSV data with a 1-second delay
for index, row in df.iterrows():
    data = row.to_json()
    socket.send_string(data)
    print(f"Published: {data}")
    time.sleep(1)

print("All data published.")
