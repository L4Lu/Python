 # Written as part of my Python learning path.
  
input_ip = input("Enter IPv4 address: ")
ip_segments = input_ip.split(".") #remove dots
if len(ip_segments) != 4: #checking if IP format is correct
    print("IPv4 address your provided is not correct.")
    quit()

ip_as_binary = [] #creating variable

for octet in ip_segments: #creating for loop
    num = int(octet) #changig strings to integers
    bin_num = bin(num) #changing integers to binaries
    ip_as_binary.append(bin_num[2:].zfill(8))# [2:] use slice to remove 0b value AND use z.fill(8) to add zeros in case of 1.1.1.1

print(".".join(ip_as_binary)) #printing converted output
