#!/usr/bin/env python3

def main():

    hash = str(input('Insert your hash: '))

    hashSalt = ":"

    hashSaltCheck = hash.split(hashSalt, 1) [0]
    hashEncoded = hashSaltCheck.encode("utf-8")

    
    if len(hashEncoded)*4 == 128 and bytes.isupper(hashEncoded) == False :
        print("MD5 Hash Detected!!")

    elif len(hashEncoded)*4 == 160:
        print("SHA1 Hash Detected!!")

    elif len(hashEncoded)*4 == 128 and  bytes.isupper(hashEncoded) == True :
        print("NTLM Hash Detected!!")

    elif len(hashEncoded)*4 == 224:
        print("SHA-224 Hash Detected!!")
    
    elif len(hashEncoded)*4 == 256:
        print("SHA-256 Hash Detected!!")

    elif len(hashEncoded)*4 == 512:
        print("SHA-512 Hash Detected")

    if len(hash) > len(hashEncoded):
        print("Possible Salted/Passed Hash!!")

    
if __name__ == "__main__":
    main()
