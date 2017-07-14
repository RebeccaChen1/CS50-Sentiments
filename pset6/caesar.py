import cs50
import sys



if len(sys.argv) != 2:
    print("missing command-line argument")
    exit(1)
key = int(sys.argv[1])

print("plaintext: ", end="")
plainText = cs50.get_string()
print("ciphertext: ", end="")

    
for i in range(len(plainText)):
    cipherText = plainText[i]
   
    if plainText[i].isupper():
     
        cipherText = ((ord(plainText[i]) - 65 + key) % 26) + 65
        cipherText = chr(cipherText)
        print("{}".format(cipherText), end="")
        
    elif plainText[i].islower():
      
        cipherText = (((ord(plainText[i])) - 97 + key) % 26) + 97
        cipherText = chr(cipherText)
        print("{}".format(cipherText), end="")
        
    else:
        print("{}".format(cipherText), end="")
        
print("")
exit(0)
