import zmq
import json

# Initialize socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:8080")  # Connect to port 8080


location = input("Enter a location name or coordinates (format: lat,long): ")


socket.send_string(location)

# Receive JSON response with coordinates
message = socket.recv_string()
coordinates = json.loads(message)


print(f"Coordinates for {location}: {coordinates}")
