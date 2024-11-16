import zmq
import json
from geopy.geocoders import Nominatim

# Function to get coordinates using Geopy if a location name is provided
def get_coordinates(location):
    geolocator = Nominatim(user_agent="geo_microservice")
    location_data = geolocator.geocode(location)

    if location_data:
        return {"lat": location_data.latitude, "long": location_data.longitude}
    return {"lat": None, "long": None}

# Check if input is in "lat,long" format
def is_coordinates_format(location):
    try:
        lat, lon = map(float, location.split(","))
        return {"lat": lat, "long": lon}
    except ValueError:
        return None

# Initialize ZMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8080")

print("Server is running...")

while True:
    # Receive location request from the client
    location = socket.recv_string()
    print(f"Received request for location: {location}")

    # Check if location is in coordinate format
    coordinates = is_coordinates_format(location)
    if not coordinates:  # If not coordinates, treat it as a place name
        coordinates = get_coordinates(location)

    # Send JSON response with latitude and longitude
    response = json.dumps(coordinates)
    socket.send_string(response)
