from src.soporte import calculate_mortage

# We define the mortgage parameters

due = 10000 # Variable with the total amount due
interest = 0.5 / 100 # Variable with the monthly interest divided by 100 to calculate the percentage. 
monthly_payment = 375 # Variable with the monthly payment
yearly_extra_payment = 500 # Variable with the extra payment that is made every 12 months 


calculate_mortage(due, interest, monthly_payment, yearly_extra_payment) # We call the function


print("Now, define your own parameters!")

due2 = float(input("Introduce your total amount due: "))
interest2 = float(input("Introduce your monthly interest: ")) / 100
monthly_payment2 = float(input("Introduce your monthly payment: "))
yearly_extra_payment2 = float(input("Introduce your yearly extra payment: "))

calculate_mortage(due2, interest2, monthly_payment2, yearly_extra_payment2)

