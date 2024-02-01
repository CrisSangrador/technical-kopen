import csv

def calculate_mortage(due, interest, monthly_payment, yearly_extra_payment, name_csv): # We define the function with the parameters that will be established in the main.py file
    
    """This function receives five parameters:
    - due (float): the total amount due.
    - interest (float): the monthly interest rate
    - monthly_payment (float): the amount paid each month
    - yearly_extra_payment (float): the extra amout that is paid every 12 months
    - name_csv (str): the name in which we want to save the CSV file that will contain the output
    
    The output is a print that shows the different information for each month until the mortgage is totally paid off."""


    month = 1 # We set the month variable to 1

    #We create a csv to write the information on it
    with open(name_csv, "w", newline = "") as file:
        writer = csv.writer(file)

    # We add the headers to the csv file as well as the first row
        writer.writerow(["Month", "Interest", "Due", "Due with interest", "To pay"])
        writer.writerow([month, (due * interest), due, (due + (due * interest)), monthly_payment])

    # We print the first month's information

    print(f"Month: {month}, interest: {due * interest:.2f}, due: {due:.2f}, due + interest: {due + (due * interest):.2f}, to pay {monthly_payment}")
    
    # We create a while loop to calculate the mortage payments as long as the due amount is greater than the established monthly payment

    while due > monthly_payment: 
        
        month += 1 # We add a month for each time the loop runs

        payment = monthly_payment

        if month % 12 == 0: # We create an 'if' condition so if the number of the month is divisible by 12 to add the yearly extra payment if necessary
            
            payment = monthly_payment + yearly_extra_payment


        due_with_interest = due + (due * interest)

        print(f"Month: {month}, interest: {due * interest:.2f}, due: {due:.2f}, due + interest: {due_with_interest:.2f}, to pay {payment}")

                    # We write the info in the CSV
        with open(name_csv, "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([month, (due * interest), due, due_with_interest, (payment)])

        # We calculate the new due amount by substracting the monthly and yearly payment
        
        due = due_with_interest - (payment)


    else: # Once the due amount is less than the monthly payment

        month += 1
        
        # We calculate the new due amount
        due = due + (due * interest) 

        # We add the interest rate
        due_with_interest = due + (due * interest) 

        # We equate the monthly payment to the amount due
        monthly_payment = due_with_interest 

        #We print the month's info        
        print(f"Month: {month}, interest: {due * interest:.2f}, due: {due:.2f}, due + interest: {due_with_interest:.2f}, to pay {monthly_payment:.2f}")

        # We write the info in the CSV
        with open(name_csv, "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([month, (due * interest), due, due_with_interest, monthly_payment])
    