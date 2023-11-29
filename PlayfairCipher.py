
def table(key):
    global mat
    mat = [[0 for i in range(5)] for j in range(5)]
    arr = [0 for i in range(26)]
    k = 0
    j = 0
    for i in range(len(key)):
        if key[i] == 'J':
            key[i] = 'I'
        if arr[ord(key[i])-65] == 0:
            mat[j][k] = key[i]
            k += 1
            if k == 5:
                k = 0
                j = j+1
            arr[ord(key[i])-65] = 1
    for i in range(26):
        if arr[i] == 0 and chr(i+65) != 'J':
            mat[j][k] = chr(i+65)
            k += 1
            if k == 5:
                k = 0
                j = j+1
    for i in range(5):
        for j in range(5):
            print(mat[i][j], end=" ")
        print("\n")


def eneycrypt(str):
    global mat
    result = ""
    if len(str) % 2 != 0:
        str += 'X'
    for i in range(0, len(str), 2):
        i1, j1, i2, j2 = 0, 0, 0, 0
        a, b = str[i], str[i + 1]
        if str[i] == str[i+1]:
                b = 'X'
        for j in range(5):
            for k in range(5):
                if mat[j][k] == a:
                        i1 = j
                        j1 = k
                if mat[j][k] == b:
                        i2 = j
                        j2 = k
        result += mat[i1][j2]
        result += mat[i2][j1]
    return result


def decrypt(str):
    result=""
    for i in range(len(str)-1):
        if str[i]=='X' and 0<i and i<len(str)-1:
            result+=str[i-1]
        else:
            result+=str[i]
    if str[len(str)-1]!='X':
        result+=str[len(str)-1]
    return result
            
str = input("Enter the string: ")
str=str.upper()
key=input("Enter the key: ")
key=key.upper()
while True:
    option=int(input("Enter 1 to encrypt\nEnter 2 to decrypt\nEnter 3 to exit: \n"))
    if option==1:
        table(key)
        enycrypt_str=eneycrypt(str)
        print("Encrypted string: ",enycrypt_str)
    elif option==2:
        enycrypt_str=eneycrypt(enycrypt_str)
        decrypt_str=decrypt(enycrypt_str)
        print("Decrypted string: ",decrypt_str)
    else:
        break
