import timeit
stmt1='''
func_one(100)
'''
setup1='''
def func_one(n):
    return [str(num) for num in range (n)]
'''
stmt2='''
func_two(100)
'''
setup2='''
def func_two(n):
    return list(map(str,range(n)))
'''
timer1=timeit.timeit(stmt1,setup1,number=10000)
print(timer1)
timer2=timeit.timeit(stmt2,setup2,number=10000)
print(timer2)