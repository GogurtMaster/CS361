import zmq
import json
import math


def coordinates_close(coord1, coord2):
    """
    Compare two coordinate dictionaries with a tolerance for floating-point values.
    """
    if coord1["lat"] is None or coord2["lat"] is None:
        return coord1["lat"] == coord2["lat"] and coord1["long"] == coord2["long"]

    return (
        math.isclose(coord1["lat"], coord2["lat"], abs_tol = 0.0001)
        and math.isclose(coord1["long"], coord2["long"], abs_tol = 0.0001)
    )


def run_server():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:8080")

    print("Testing the microservice...\n")


def test_microservice():
    # Initialize ZMQ
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:8080")

    # Define test cases: location names, coordinates, and invalid input
    test_cases = [
        ("New York", {"lat": 40.7127281, "long": -74.0060152}),  # Example city
        ("45.516, -122.678", {"lat": 45.516, "long": -122.678}), # Valid coordinates
        ("Albany", {"lat": 42.6511674, "long": -73.754968}),     # Another city
        ("UnknownLocationName", {"lat": None, "long": None})     # Non-existent location
    ]

    for location, expected_response in test_cases:
        # Send test input to the server
        socket.send_string(location)
        
        # Receive response from server
        message = socket.recv_string()
        response = json.loads(message)

        # Compare response with the expected result
        passed = coordinates_close(response, expected_response)

        # Print test result
        print(f"Input: {location}")
        print(f"Response: {response}")
        print(f"Expected: {expected_response}")
        print(f"Test Passed: {passed}\n")


if __name__ == "__main__":
    run_server()
    test_microservice()
