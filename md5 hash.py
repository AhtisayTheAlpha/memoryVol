# Python program to find MD5 hash value of a file
import hashlib


def hash_file(filename):
    #filename = input("C:/Users/Imesha/Downloads/Programs/pbsvc.exe")
    with open(filename,"rb") as f:
        bytes = f.read() # read file as bytes
        readable_hash = hashlib.md5(bytes).hexdigest();
        print(readable_hash)

message = hash_file("C:/Users/Imesha/Downloads/Programs/pbsvc.exe")
