

def enycrypt(str,key):
    result = ""
    for i in range(len(str)):
        if str[i].isupper():
            result+=chr((ord(str[i])+key-65)%26+65)
        elif str[i].islower():
           result+=chr((ord(str[i])+key-97)%26+97)
        else:
            result+=str[i]
    return result

def decrypt(str,key):
    result = ""
    for i in range(len(str)):
        if str[i].isupper():
            result+=chr((ord(str[i])-key-65)%26+65)
        elif str[i].islower():
           result+=chr((ord(str[i])-key-97)%26+97)
        else:
            result+=str[i]
    return result

flag=False
while True:
    option=int(input("Enter 1 to encrypt, 2 to decrypt, 3 to exit: "))
    if option==1:
        if flag is True:
            print("Already encrypted, please decrypt first")
        else:
            flag=True
            str=input("Enter the string: ")
            enycrypt_str=enycrypt(str,3)
            print("Encrypted string: ",enycrypt_str)
    elif option==2:
        if flag is not True:
            print("Please encrypt first")
        else:
            flag=False
            decrypt_str=decrypt(enycrypt_str,3)
            print("Decrypted string: ",decrypt_str)
    else:
        break