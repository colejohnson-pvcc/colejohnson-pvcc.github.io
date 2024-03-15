# Name: Cole Johnson
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
# define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#define global variables
inout = 1  # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0


##############  define program functions ##############
def main():

    another_student = True
    while another_student:
        get_user_data()
        perform_calculations()
        display_results()
        
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            another_student = False
            print("Thank you for enrolling at PVCC. Enjoy the semester!")

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global in_state_tuition, out_of_state_tuition, capital_fee, institution_fee, activity_fee, total, scholarship_amount, balance
    in_state_tuition = numcredits * RATE_TUITION_IN
    out_of_state_tuition = numcredits * RATE_TUITION_OUT
    capital_fee = numcredits * RATE_CAPITAL_FEE
    institution_fee = numcredits * RATE_INSTITUTION_FEE
    activity_fee = numcredits * RATE_ACTIVITY_FEE
    
    if inout == 1:
        total = numcredits * RATE_TUITION_IN + institution_fee + activity_fee
        balance = total - scholarshipamt
    else:
        total = numcredits * RATE_TUITION_OUT + capital_fee + institution_fee + activity_fee
        balance = total - scholarshipamt
    

def display_results():
    if inout == 1:
        print('In-State Tuiton         $ ' + format(in_state_tuition,'8,.2f'))
        print('Institution Fee         $ ' + format(institution_fee,'8,.2f'))
        print('Activity Fee            $ ' + format(activity_fee,'8,.2f'))
        print('Total                   $ ' + format(total,'8,.2f'))
        print('Scholarship             $ ' + format(scholarshipamt,'8,.2f'))
        print('Balance                 $ ' + format(balance,'8,.2f'))
        print('------------------------------')
        print(str(datetime.datetime.now()))
    else:
        print('Out-of-State Tuition    $ ' + format(out_of_state_tuition,'8,.2f'))
        print('Capital Fee             $ ' + format(capital_fee,'8,.2f'))
        print('Institution Fee         $ ' + format(institution_fee,'8,.2f'))
        print('Activity Fee            $ ' + format(activity_fee,'8,.2f'))
        print('Total                   $ ' + format(total,'8,.2f'))
        print('Scholarship             $ ' + format(scholarshipamt,'8,.2f'))
        print('Balance                 $ ' + format(balance,'8,.2f'))
        print('------------------------------')
        print(str(datetime.datetime.now()))

##########  call on main program to execute ##########
main()

