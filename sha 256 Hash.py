# Python program to find SHA256 hexadecimal hash string of a file
import hashlib

def hash_file(filename):
    #filename = input("Enter the input file name: ")
    with open(filename,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        print(readable_hash)

message = hash_file("C:/Users/Imesha/Downloads/Programs/pbsvc.exe")
