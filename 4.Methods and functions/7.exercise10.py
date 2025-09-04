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
def blackjack(a,b,c):
    summation=a+b+c
    if summation<=21:
        return summation
    elif summation>21 and a==11 or b==11 or c==11 :
        summation-=10
        return summation
    else:
        print("BUST")
        
def has_33(nums):
    for i in range (len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
