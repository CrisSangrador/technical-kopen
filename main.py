from src.support import calculate_mortage

# We define the mortgage parameters

due = 10000 # Variable with the total amount due
interest = 0.5 / 100 # Variable with the monthly interest divided by 100 to calculate the percentage. 
monthly_payment = 375 # Variable with the monthly payment
yearly_extra_payment = 500 # Variable with the extra payment that is made every 12 months 

name_csv = "mortgage.csv"


calculate_mortage(due, interest, monthly_payment, yearly_extra_payment, name_csv) # We call the function

reply = input("Now, do you want to define your own parameters? ")

if reply.lower() == "yes":

    due2 = float(input("Introduce your total amount due: "))
    interest2 = float(input("Introduce your monthly interest: ")) / 100
    monthly_payment2 = float(input("Introduce your monthly payment: "))
    yearly_extra_payment2 = float(input("Introduce your yearly extra payment: "))
    name_csv2 = input("Introduce the name you want to give to your CSV file: ")
    
    calculate_mortage(due2, interest2, monthly_payment2, yearly_extra_payment2, name_csv2)


else: 
    pass
