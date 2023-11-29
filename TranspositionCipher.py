

def enycrypt(str,key):
    result = ""
    temp=len(str)/len(key)
    if len(str)%len(key)!=0:
        temp+=1
    mat=[[" " for i in range(len(key))] for j in range(int(temp))]
    k=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if len(str)>k:
                mat[i][j]=str[k]
                k+=1
    temp=key
    temp=sorted(temp)
    for i in range(len(temp)):
        for j in range(len(key)):
            if temp[i]==key[j]:
                col=j
                break
        for j in range(len(mat)):
            result+=mat[j][col]
    return result

def decrypt(str,key):
    result = ""
    temp=len(str)/len(key)
    if len(str)%len(key)!=0:
        temp+=1
    mat=[[" " for i in range(len(key))] for j in range(int(temp))]
    temp=key
    temp=sorted(temp)
    for i in range(len(temp)):
        for j in range(len(key)):
            if temp[i]==key[j]:
                col=j
                break
        for j in range(len(mat)):
            mat[j][col]=str[i*len(mat)+j]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            result+=mat[i][j]
    return result
        
            

input_str=input("Enter the string: ")
input_key=input("Enter the key: ")
enycrypt_str=enycrypt(input_str,input_key)
print("Encrypted string: ",enycrypt_str)
decrypt_str=decrypt(enycrypt_str,input_key)
print("Decrypted string: ",decrypt_str)