# Implementation of a brute-force decryption algorithm using ASCII characters. 
# It attempts to decrypt an encrypted message by trying different ASCII characters 
# and checking if the resulting encrypted message matches the given secret.
# Decode "6c12fc21028cc7536c" to "Well Done".

import socket
import string

def main():
    print("Main function is running")
    ascii_table = string.printable
    secret = input("Encrypted message: ")
    decrypted = ""
    while True:
        initial_decrypted = decrypted
        for char in ascii_table:
            #print(char)
            encrypted = get_encrypted_message(decrypted + char)
            if secret.startswith(encrypted):
                print("Decrypted character: " + char)
                decrypted += char
            if encrypted == secret:
                print("Decrypted answer: " + decrypted)
                return
        if initial_decrypted == decrypted:
            print("Unable to decrypt using ASCII brute-force.")
            return 

def get_encrypted_message(txt):
    my_socket = socket.socket()
    server_details = ("127.0.0.1", 1334)
    my_socket.connect(server_details)
    my_socket.recv(1024).decode()
    #print(my_socket)
    my_socket.send(txt.encode())
    encrypted = my_socket.recv(1024).decode()
    my_socket.close()
    return encrypted
    

if __name__ == "__main__":
    main()
    
