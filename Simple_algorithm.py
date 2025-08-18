# Simple_algorithm

address = "198.223.XX.XX"

# Extract the first thee characters of an IP address
print(address[0:3])

IP = ["198.223.xx.xx", "198.101.xx.xx", "180.064.xx.xx", "192.168.xx.xx", "184.090.xx.xx"]

# Extract the first three characters from a list of IP addresses
networks = [] # creating an empty list
for address in IP: # starting a for loop, list IP as an iterable
    networks.append(address[0:3]) # inside the for loop  to get the first 3 characters of the list
print(networks)