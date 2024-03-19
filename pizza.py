# Name: Cole Johnson
# Prog Purpose: This program finds the cost of pizzas
#   Price for one small pizza: $9.99
#   Price for one medium pizza: $12.99
#   Price for one large pizza: $17.99
#   Price for one extra large pizza: $21.99
#   Price of a drink: $3.99
#   Price for breadsticks: $6.99
#   Sales tax rate: 5.5%

import datetime

##############  define global variables ##############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_SMALL_PIZZA = 9.99
PR_MEDIUM_PIZZA = 12.99
PR_LARGE_PIZZA = 17.99
PR_EXTRA_LARGE_PIZZA = 21.99
PR_DRINK = 3.99
PR_BREADSTICK = 6.99

# define global variables
size = 1
num_small_pizzas = 0
num_medium_pizzas = 0
num_large_pizzas = 0
num_extra_large_pizzas = 0
num_drinks = 0
num_breadstick_orders = 0
subtotal = 0
sales_tax = 0
total = 0

##############  define program functions ##############
def main():

    more_pizzas = True

    while more_pizzas:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == "N" or yesno =="n":
            more_pizzas = False
            print("Thank you for your order. Enjoy your pizza!")

def get_user_data():
    print('------------------------------')
    print('  **** Palermo Pizza ****')
    print('------------------------------')
    print('Small Pizza            $9.99')
    print('Medium Pizza           $12.99')
    print('Large Pizza            $17.99')
    print('Extra Large Pizza      $21.99')
    print('Drink                  $3.99')
    print('Breadsticks            $6.99')
    print('------------------------------')
    global size
    size = input("\nWhat size pizza would you like to order?(S for small, M for medium, L for large, X for extra large): ")
    global num_small_pizzas
    if size == "s" or size == "S":
        num_small_pizzas = int(input("Number of small pizzas: "))
    global num_medium_pizzas
    if size == "m" or size == "M":
        num_medium_pizzas = int(input("Number of medium pizzas: "))
    global num_large_pizzas
    if size == "l" or size == "L":
        num_large_pizzas = int(input("Number of large pizzas: "))
    global num_extra_large_pizzas
    if size == "x" or size == "X":
        num_extra_large_pizzas = int(input("Number of extra large pizzas: "))
    global num_drinks
    num_drinks = int(input("Number of drinks: "))
    global num_breadstick_orders
    num_breadstick_orders = int(input("Number of breadstick orders: "))
    
def perform_calculations():
    global subtotal, sales_tax, total
    if size == "s" or size == "S":
        subtotal = num_small_pizzas * PR_SMALL_PIZZA + num_drinks * PR_DRINK + num_breadstick_orders * PR_BREADSTICK
        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax
    if size == "m" or size == "M":
        subtotal = num_medium_pizzas * PR_MEDIUM_PIZZA + num_drinks * PR_DRINK + num_breadstick_orders * PR_BREADSTICK
        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax
    if size == "l" or size == "L":
        subtotal = num_large_pizzas * PR_LARGE_PIZZA + num_drinks * PR_DRINK + num_breadstick_orders * PR_BREADSTICK
        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax
    if size == "x" or size == "X":
        subtotal = num_extra_large_pizzas * PR_EXTRA_LARGE_PIZZA + num_drinks * PR_DRINK + num_breadstick_orders * PR_BREADSTICK
        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax
        
def display_results():
    print('------------------------------')
    print('  **** Palermo Pizza ****')
    print('------------------------------')
    if size == "s" or size == "S":
        print('Number of pizzas ordered: '+ format(num_small_pizzas,'2.0f'))
        print('Small Pizza          $ ' + format(num_small_pizzas * PR_SMALL_PIZZA,'8,.2f'))
        print('Drink                $ ' + format(num_drinks * PR_DRINK,'8,.2f'))
        print('Breadsticks          $ ' + format(num_breadstick_orders * PR_BREADSTICK,'8,.2f'))
        print('Subtotal             $ ' + format(subtotal,'8.2f'))
        print('Sales Tax            $ ' + format(sales_tax,'8,.2f'))
        print('Total                $ ' + format(total,'8,.2f'))
        print('------------------------------')
    if size == "m" or size == "M":
        print('Number of pizzas ordered: '+ format(num_medium_pizzas,'2.0f'))
        print('Medium Pizza         $ ' + format(num_medium_pizzas * PR_MEDIUM_PIZZA,'8.2f'))
        print('Drink                $ ' + format(num_drinks * PR_DRINK,'8,.2f'))
        print('Breadsticks          $ ' + format(num_breadstick_orders * PR_BREADSTICK,'8,.2f'))
        print('Subtotal             $ ' + format(subtotal,'8.2f'))
        print('Sales Tax            $ ' + format(sales_tax,'8,.2f'))
        print('Total                $ ' + format(total,'8,.2f'))
        print('------------------------------')   
    if size == "l" or size == "L":
        print('Number of pizzas ordered: '+ format(num_large_pizzas,'2.0f'))
        print('Large Pizza          $ ' + format(num_large_pizzas * PR_LARGE_PIZZA,'8.2f'))
        print('Drink                $ ' + format(num_drinks * PR_DRINK,'8,.2f'))
        print('Breadsticks          $ ' + format(num_breadstick_orders * PR_BREADSTICK,'8,.2f'))
        print('Subtotal             $ ' + format(subtotal,'8.2f'))
        print('Sales Tax            $ ' + format(sales_tax,'8,.2f'))
        print('Total                $ ' + format(total,'8,.2f'))
        print('------------------------------')
    if size == "x" or size == "X":
        print('Number of pizzas ordered: '+ format(num_extra_large_pizzas,'2.0f'))
        print('Extra Large Pizza    $ ' + format(num_extra_large_pizzas * PR_EXTRA_LARGE_PIZZA,'8.2f'))
        print('Drink                $ ' + format(num_drinks * PR_DRINK,'8,.2f'))
        print('Breadsticks          $ ' + format(num_breadstick_orders * PR_BREADSTICK,'8,.2f'))
        print('Subtotal             $ ' + format(subtotal,'8.2f'))
        print('Sales Tax            $ ' + format(sales_tax,'8,.2f'))
        print('Total                $ ' + format(total,'8,.2f'))
        print('------------------------------')
    print(str(datetime.datetime.now()))        

##########  call on main program to execute ##########
main()

