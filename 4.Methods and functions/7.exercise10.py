def myfunc(stri):
    result=''
    for x in range(len(stri)):
        if x%2==0:
            result+=stri[x].upper()
        else:
            result+=stri[x].lower()
    return result
print(myfunc('Beni'))
print(max(1,2))
