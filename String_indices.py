# String indices and slices
print("HELLO"[1])

# Extract a slice from a string
print("HELLO"[1:4])

# Use the index string method
print("HELLO".index("E"))

# Search for the character "L"
print("HELLO".index("L"))

# Strings are immutable
# my_string = "HELLO"
# my_string[1] = "A"

# Bracket notation
device_id = "h32rb17"
print("h32rb17"[0])
print(device_id[0])

# slice from a string
print("h32rb17"[0:3])

# str() and len() functions
device_id_length = len("h32rb17")
if device_id_length == 7:
    print("The device ID has 7 characters.")
    
# .upper() and .lower() methods
print("h32rb17".index("r"))

# index method
print("r45rt46".index("r"))

# Finding substrings with .index()
tshah_index = "tsnow, tshah, bmoreno - updated".index("tshah")
print(tshah_index)