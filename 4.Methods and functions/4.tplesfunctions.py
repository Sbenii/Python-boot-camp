#Tuples unpacking with python functions
def employee_check(work_hours):
    max_hours=0
    best_employee=''
    for employee,hours in work_hours:
        if hours>=max_hours:
            max_hours=hours
            best_employee=employee
        else:
            pass
    return(best_employee,max_hours)
Monthly_report=[('Andy',239),('Miguel',347),('Quessy',98),('Linda',321)]
print(employee_check(Monthly_report))
name,time=employee_check(Monthly_report)
print(f"The employee of the month: {name}")
print(f"The most time by an active employee: {time} hours")
