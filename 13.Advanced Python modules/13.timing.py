import time
def func_one(n):
    return [str(num) for num in range (n)]

def func_two(n):
    return list(map(str,range(n)))

#For func one
#Time before running the code
start_time=time.time()
#run code
result=func_one(10)
#Time after running the code
end_time=time.time()
#elapsed time
elapsed_time=end_time-start_time
print(elapsed_time)

#For func_two
#Time before running the code
start_time=time.time()
#run code
result=func_two(10)
#Time after running the code
end_time=time.time()
#elapsed time
elapsed_time=end_time-start_time
print(elapsed_time)

