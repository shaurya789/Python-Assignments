annual_salary=float(input("Enter your annual salary:  "))
portion_saved=float(input("Enter the percent of income saved as a decimal: "))
cost=float(input("Enter the total cost of the house:  "))
semi_annual_raise=float(input('Enter the semi annual raise percent as a decimal:  '))

promo = 0
month=0
down=0.25*cost #downpayment 
rate=0.04 #rate of interest annually
saving=0


while saving < down:
    if month%6 == 0 and month !=0 :
        promo = annual_salary*semi_annual_raise
        annual_salary += promo
    monthly_salary= annual_salary/12
    add_saving= monthly_salary*portion_saved   
    interest=saving*rate/12 #monthly income that is saved
    saving += add_saving + interest
    month += 1
    
print("Number of months: ", month)


    
