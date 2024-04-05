# Name: Cole Johnson
# Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global salestax, occupancy, subtotal, total, grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
#STUDENTS: COMPLETE THESE elif AND else statements
            elif room_type =="DR":
                subtotal = ROOM_RATES[1] * num_nights

            else:
                subtotal = ROOM_RATES[2] * num_nights
                
#STUDENTS: COMPLETE THESE CALCULATIONS        
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total     = subtotal + salestax + occupancy
            grandtotal += total
        
#STUDENTS: ADD THE REST OF THE append statements after this one       
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)
            guest[i].append(grandtotal)



def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: center} </style> </head>\n')
    f.write('<body style = "background-color: #4eb4dd; background: url(wp-beach.jpg); color: #e9e2bf;">\n')  #STUDENTS: COMPLETE THIS STATEMENT
    
def create_output_html():
    global f
    
    currency="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "8">'

 #STUDENTS: INSERT ALL THE MISSING f.write STATEMENTS HERE
    f.write('\n<table border="3"   style ="background-color: #51bedf;  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2 style = "text-align: center; padding-top: 20px"> Emerald Beach Hotel & Resort Guest Report </h2></tr>')
    f.write(colsp + '\n')
    titles1 = '<h3 style = "padding-top: 20px"> Guest Sales Report: ' + day_time + '</h3>'
    f.write(titles1)
    f.write('<tr><td> Last Name</td><td> First Name</td><td> Room Type</td><td> Num Nights</td><td> Subtotal</td><td> Sales Tax</td><td> Occupancy Tax</td><td> Total</td></tr>')
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])
            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
                
            elif room_type =="DR":   
                subtotal = ROOM_RATES[1] * num_nights
            
            else:
                subtotal = ROOM_RATES[2] * num_nights

            
            data1 = guest[i][0] + "\t" + td + guest[i][1]+ "" + td + guest[i][2] + "\t" + td + guest[i][3] + "\t" + td + format(subtotal,currency) + td + format(salestax,currency) + td + format(occupancy,currency) + td + format(total,currency) + endtr
            f.write(tr + data1 + endtr)

    f.write(colsp + 'Grand Total = ' + format(grandtotal,currency))
    f.write('</table><br />')
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')

##call on main program to execute##
main()
