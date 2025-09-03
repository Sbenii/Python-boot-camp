def even_check(nbr):
    return nbr%2==0
print(even_check(238784938))
#Return true if any number in the list is even
def even_list_checker(num_list):
    for nbr in num_list:
        if nbr %2==0:
            return True
    return False
print(even_list_checker([1,4,5,7,8675,3437,557,32]))
#Return even numbers of the list
def even_num_ret(num_list):
    evennum=[]
    for nbr in num_list:
        if nbr %2==0:
           evennum.append(nbr)
        else:
            pass
    return evennum
print(even_num_ret([1,4,5,8,8675,3437,557,32]))