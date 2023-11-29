def palindrom(str):
    for i in range(int(len(str)/2)):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True

while True:
    str=input("enter the string  :")
    print(len(str))
    flag=palindrom(str)

    if flag is True:
        print("string is plaindrome")
    else:
        print("string is not palindome")