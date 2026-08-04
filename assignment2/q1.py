#calculate the final tax rate based on these rule
salary=int(input("Enter your salary:"))
if salary<30000:
    print(5*salary/100,"tax")#if salary<30000-> 5%
elif 30000<=salary<=70000:
    print(15*salary/100,"tax")#if salary is 30000-70000-> 15%
else:
    print(25*salary/100,"tax")#if salary is >70000-> 15%

    
