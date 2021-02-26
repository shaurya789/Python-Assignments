salary=float(input("Enter your annual salary: $"))
x= salary
cost = 1000000
semi_annual_raise = 0.07

low = 0
high = 10000
down=0.25*cost #downpayment 
interest=0.04 #rate of interest annually
saving=0.0
n=0

c_saving=0.0 #values to check if down is possible
c_month= 0
c_salary = salary

while c_month < 36: #loop to check if down payment is possible if I save all montly income
    if c_month%6 == 0 and c_month !=0 :
        promo = c_salary*semi_annual_raise
        c_salary += promo
    c_monthly_salary = c_salary/12
    c_saving += c_monthly_salary + c_saving*interest/12
    c_month += 1

if c_saving >= (down - 100.0):
    
    while abs(down-saving)>100:
        portion_saved = (low + high)/2
        saving = 0.0
        salary=x
        
        for month in range(36):
            monthly_salary=salary/12.0
            additional = float(monthly_salary*portion_saved/10000)
            saving += ( additional + float(saving*interest/12.0 ))
            if month%6 ==0 and month != 0:
                salary += (semi_annual_raise*salary)
              
        if down - saving > 100.0:
            low = portion_saved
            
        elif saving- down> 100.0:
            high = portion_saved

        n+= 1
    
    print("The percentage of monthly income that you should save is",portion_saved/100,"%")
    print("The number of tries in bisection search is",n)
    print("After 36 months you end up saving $",saving)
    
else:
    print("It is not possible to save for a down payment")


    
