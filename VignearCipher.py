mat=[[0 for i in range(26)] for j in range(26)]
def table():
    global mat
    mat=[[0 for i in range(26)] for j in range(26)]
    for i in range(26):
        for j in range(26):
            mat[i][j]=chr((i+j)%26+65)
    return mat
            

def encrypted(str,key):
    global mat
    while len(key)<len(str):
        key+=key
    result=""
    for i in range(len(str)):
        row=ord(str[i])-65
        col=ord(key[i])-65
        if not str[i].isspace():
            result+=mat[row][col]
        else:
            result+=" "
    return result
def decrypt(str,key):
    result=""
    while len(key)<len(str):
        key+=key
    for j in range(len(str)):
        col=ord(key[j])-65
        for i in range(26):
            if not str[j].isspace() and mat[i][col]==str[j]:
                result+=chr(i+65)
            elif str[j].isspace():
                result+=" "
                break
    return result
    
    
table()
str=input("Enter the string: ")
key=input("Enter the key: ")
str=str.upper()
key=key.upper()
while True:
    opt=input("Enter 1 for Enycryption\nEnter 2 for Decryption\nEnter 3 to exit: ")
    print(opt)
    if int(opt)==1:
        enycrypt_str=encrypted(str,key)
        str=enycrypt_str
        print("Encrypted string: ",enycrypt_str)
    elif int(opt)==2:
        decrypt_str=decrypt(str,key)
        str=decrypt_str
        print("Decrypted string: ",decrypt_str)
    else:
        break

    
    