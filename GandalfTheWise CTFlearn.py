#!/usr/bin/python

import base64

# ciphers grabbed from Gandalf.jpg strings
cipher1 = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
cipher2 = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"

#convert ciphers to base64
b64 = cipher1
b64_2 = cipher2

b64_bytes = base64.b64decode(b64)
b64_bytes2 = base64.b64decode(b64_2)

#convert base64 to hexadecimal values
hex1 = b64_bytes.hex()
hex2 = b64_bytes2.hex()

print("hexadecimal values:")
print(hex1)
print(hex2)

#hex1 = "c43ea47ced94ac4e529cb43a5a01122b892f0ff63fac324f5cd538e64fe9"
#hex2 = "876ae21088f5de2029dbd5543e607e4da76d669a5dc3702e3bb251883c94"

# Find the length of the longer value
max_len = max(len(hex1), len(hex2))

# Pad the shorter value with zeros using zfill()
hex1 = hex1.zfill(max_len)
hex2 = hex2.zfill(max_len)

print(hex1)
print(hex2)

# Use zip() to pair up the hexadecimal digits from both values
pairs = zip(hex1, hex2)

# Use ^ operator to XOR each pair of digits
xor_digits = [int(a, 16) ^ int(b, 16) for a, b in pairs]

# Convert the XORed digits to hexadecimal characters using hex()
# and remove the '0x' prefix using slicing
xor_chars = [hex(d)[2:] for d in xor_digits]

# Join the hexadecimal characters into a string
xor_string = "".join(xor_chars)

# Convert the hexadecimal string to bytes using bytes.fromhex()
xor_bytes = bytes.fromhex(xor_string)

# Decode the bytes to a string using latin-1 encoding
xor_text = xor_bytes.decode("latin-1")

# Print the result and the flag
print(xor_text)
