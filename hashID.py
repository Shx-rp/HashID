#!/usr/bin/env python3
import os

def main():

    hash = str(input('Insert your hash: '))

    hashSalt = ":"

    hashSaltCheck = hash.split(hashSalt) [0]
    hashEncoded = hashSaltCheck.encode("utf-8")
    #print(len(hashEncoded)*4)

    print("-------------------------------------")
    if len(hashEncoded)*4 == 128 and bytes.isupper(hashEncoded) == False :
        print("\n\n|MD5 Hash Detected !!\n")
        if len(hash) > len(hashEncoded):
            print("\n|Salted/Passed Hash\n")
            salt = hash.split(hashSalt) [1]
            print("\n|Salt/Pass :{0} \n".format(salt))

    elif len(hashEncoded)*4 == 160:
        print("\n\n|SHA1 Hash Detected !!\n")
        if len(hash) > len(hashEncoded):
            print("\n|Salted/Passed Hash\n")
            salt = hash.split(hashSalt) [1]
            print("\n|Salt/Pass :{0} \n".format(salt))

    elif len(hashEncoded)*4 == 128 and  bytes.isupper(hashEncoded) == True :
        print("\n\n|NTLM Hash Detected !!\n")

    elif len(hashEncoded)*4 == 224:
        print("\n\n|SHA-224 Hash Detected !!\n")
    
    elif len(hashEncoded)*4 == 256:
        print("\n\n|SHA-256 Hash Detected !!\n")
        if len(hash) > len(hashEncoded):
            print("\n|Salted/Passed Hash\n")
            salt = hash.split(hashSalt) [1]
            print("\n|Salt/Pass :{0} \n".format(salt))
   
    elif len(hashEncoded)*4 == 512:
        print("\n\n|SHA-512 Hash Detected !!\n")
        if len(hash) > len(hashEncoded):
            print("\n|Salted/Passed Hash\n")
            salt = hash.split(hashSalt) [1]
            print("\n|Salt/Pass :{0} \n".format(salt))
    
    if hash.find("$BLAKE2$") == 0:
        print("\n\n|BLAKE2b-512 Hash Detected !!\n")
    
    if hash.startswith("$krb5") == 1:
        etype = hash.split("$") [2]
        user = hash.split("$") [3]
        if hash.find("$krb5pa$") == 0:
            realm = hash.split("$") [4]
            salt = hash.split("$") [5] 
            print("\n\n|Kerberos 5 Pre-Auth Hash Detected !!")
            print("|eType: {0} \n|User: {1} \n|Realm: {2} \n|Salt: {3}\n".format(etype, user, realm, salt))
        
        elif hash.find("$krb5tgs$") == 0:
            host = hash.split("$") [5]
            print("\n\n|Kerberos 5 TGS-REP Hash Detected !!")
            print("|eType: {0} \n|User: {1} \n|Ream: {2} \n|Host: {4}\n".format(etype, user, realm, host))

        elif hash.find("$krb5asrep$") == 0:
            print("\n\n|Kerberos 5 AS-REP Hash Detected !!")
            print("|eType: {0} \n|User/Host: {1}\n".format(etype, user))
    
    if len(hashEncoded) < 16:
        print("\n\n|Unsupported Hash Inserted !!\n")
    

    print("\n-------------------------------------")

    
if __name__ == "__main__":
    main()
