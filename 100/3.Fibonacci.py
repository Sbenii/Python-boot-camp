
def fibonnacci_series(x):
    t1=0
    t2=1
    while x<0:
        x=int(input(("Please enter a valid nth number!: ")))
    
    print(f"Fibonacci series:\n{t1}\n{t2}")
    for i in range (x-2):
        t3=t1+t2
        print(f"{t3}")
        t1=t2
        t2=t3

n=int(input("Enter the nth number for a fibonacci serie: "))
fibonnacci_series(n)