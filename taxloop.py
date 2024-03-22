# Name: Cole Johnson
# Prog Purpose: This program uses lists to find the personal property tax for vehicles in Charlottesville
#   and produces a report which displays all data and the total tax due
#
# Personal property tax in Charlottesville:
#       -- $4.20 per $100 of vehicle value (4.20% per year)
#       -- Paid every six months
# Personal Property Tax Relief (PPTR):
#       -- Eligibility: Owned or leased vehicles which are perdominately used for non-business purposes & have passenger license plates
#       -- Tax relief for qualified vehicles is 33%

import datetime

################# define global variables #################
# define tax rate, service fee, and prices
PPT_RATE = .021
RELIEF_RATE = .33

# define global variables
eligible = 1
tax_due = 0
PPTR = 0
vehicle_value = 0
total = 0


################# define program functions #################

def main():
    
    more_vehicles = True

    while more_vehicles:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nDo you have another vehicle that you need to pay taxes on?: (Y or N)? ")
        if yesno == "N" or yesno =="n":
            more_vehicles = False
            print("Thank you for paying your taxes!")

def get_user_data():
    global vehicle_value
    vehicle_value = int(input("\nWhat is the assessed value of your vehicle?: "))
    global eligible
    eligible =(input("\nIs your vehicle eligible for tax relief (Y/N)?: "))
            
def perform_calculations():
    global tax_due, PPTR, total
    if eligible == "y" or eligible == "Y":
        tax_due = vehicle_value * PPT_RATE
        PPTR = tax_due * RELIEF_RATE
        total = tax_due - PPTR
    if eligible == "n" or eligible == "N":
        tax_due = vehicle_value * PPT_RATE
        PPTR = 0
        total = tax_due

def display_results():
    moneyf = '8.2f'
    line =("----------------------------------------------------------------------------")
    tab = "\t"

    print (line)
    print ("********************* PERSONAL PROPERTY TAX REPORT *********************")
    print ("                       Charlottesville, Virginia                        ")

    print ("\n\t\tRUN  DATE/TIME: " + str(datetime.datetime.now()))
    print ("\nASSESSED VALUE" + tab + tab + "  FULL TAX AMOUNT" + tab + "   RELIEF" + tab + "  TAX DUE")
    print (line)

    print (format(vehicle_value, moneyf) + tab + tab + format(tax_due, moneyf) + tab + tab + format(PPTR, moneyf) + tab + format(total, moneyf))

    print (line)
    print ("*************************************** TOTAL TAX DUE: " + tab + tab + format(total, moneyf))


main()
  
    
