# Location Microservice
when a client passes a location name or a set of coordinates onto this server it will find the coordinates and send them back to the client in a json file. <ins>**_Before using this microservice make sure to install geopy._**</ins>

## Communication Contract
### Sending Data
1. Connect to server with ZMQ, currently its using socket 8080.
2. Send request as a string.
</br>Example:
</br>location = input()
</br>socket.send_string(location)

### Recieving Data
Recieve a JSON
</br>Example:
</br>coordinates = json.loads(message)
</br>the coordinates will be sent back in this format: ("lat": lat, "long": lon)

## UML Diagram:
![SmartSelect_20241116_151510_Samsung Notes](https://github.com/user-attachments/assets/267e6cac-0923-4ee7-a94d-633ed1527c77)
