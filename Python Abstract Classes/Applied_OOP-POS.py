#RANES, ALTHEA LIEZL S.

import webbrowser

student = {}

print ("Please enter the following details: ")

menu_price = {
    # items : price
    'Soda' : 29.25, 'Bottled Water' : 20.00, 'Coffee': 20.00, 'Tea': 35.50, 'Bread' : 15.00, 'Apple' : 20.50, 'Banana' : 15.00, 'Oranges' : 25.10, 'Tapsilog' : 50.99, 'Porksilog' : 50.99
}
menu_qty = {
    # items : number
    'Soda': 4, 'Bottled Water' : 4, 'Coffee' : 2, 'Tea' : 2, 'Bread' : 1, 'Apple' : 5, 'Banana' : 5, 'Oranges' : 3, 'Tapsilog' : 5, 'Porksilog' : 4
}


add_student = 'Yes'
studentList = []
student_tmp = {}
file_name = 'ublccanteen.html'

while add_student == 'Yes':
    student_name = input('\nEnter your Name (enter "Quit" to exit): ').strip().title()
    if student_name == 'Quit':
        break
    else:
        student['sName'] = student_name
    
    student_id = input('Enter your ID (enter "quit" to exit): ').lower()
    if student_id == 'quit':
        break
    else:
        student['sId'] = student_id[:7]
    
    student_sec = input('Enter Year and Section (enter "QUIT" to exit): ').strip().upper()
    if student_sec == 'QUIT':
        break
    else:
        student['sSec'] = student_sec
    
    student['sWal'] = 150.00
    
    print()
    print(student)
    
    check_information = input('Is the information correct? (Type "YES" to confirm): ').strip().upper()
    if check_information == 'YES':
        add_student = input('Do you want to add another Student? (Type "Yes" to confirm): ').strip().title()
        print()
        a_student = student.copy()
        studentList.append(a_student)
    else:
        print('\nPlease re-enter the following details: ')
        continue

    for x in studentList:
        for y in x.keys():
            if y == 'sId':
                print(x.values())

with open(file_name,'w') as f:
    message = '''
<html>
    <head>
        <h1>
            POS System Receipt
        </h1>
        <hr>
    </head>
</html>'''
    f.write(message)

another_student = 'Yes'

while another_student == 'Yes':
    id_num = str(input("\nEnter Student ID: ")).strip()
    id_number = id_num[:7]
        
    for x in studentList:
        for sID in x.values():
            if sID == id_number:
                print("ID FOUND")
                print(sID)
                student_tmp = x
                break
            
                    
    if student_tmp != {}:
        print()
        print(student_tmp)
        print()
        call_name = student_tmp['sName']
        print("What are the orders, " + call_name + '?')

        price_amount = 0
        total_store_profit = 0
        balance = student['sWal']

        add_order = 'Yes'
        while add_order == 'Yes':
            try:
                print('Please choose from the following menu: ')
                print('Soda, Bottled Water, Coffee, Tea, Bread, Apple, Banana, Oranges, Tapsilog, Porksilog')

                order = input('Please enter your order: ').strip().title()
                
                print('\n'+ order + ': Php ' + str(menu_price[order]) + ' (' + str(menu_qty[order]) + ' remaining...)')
            except KeyError:
                print('\tInvalid choice!')
                continue
            
            orders_list = []
            try:
                qty = int(input("How many " + order + ' do you want to order?: '))
                price_amount += float(menu_price[order]) * (qty)
            except ValueError:
                print('\tInvalid Quantity')
                continue

            if price_amount > student_tmp['sWal']:
                print("\tError. Insufficient Funds.")
                break
            elif int(qty) > menu_qty[order]:
                print("\tError. Over Quantity.")
                break
            else:
                print('Current price:')
                print('Php ' + str(price_amount))
                menu_qty[order] = menu_qty[order] - int(qty)
                student_tmp['sWal'] = student_tmp['sWal'] - price_amount

                total_store_profit += price_amount
                balance -= total_store_profit
                orders_list.append(order)
                price_amount = 0

            print('Your balance is now: ' + str(student_tmp['sWal']) + '.')
            add_order = input('Do you want to add more? (Type "Yes" to confirm): ').strip().title()


            with open(file_name,'a') as f:
                message = '''
            <html>
                <body>
                    <h2>
                        Here's your receipt :
                    </h2>
                    <h3>
                        Student Information :
                    </h3>
                    <p>
                    '''+ str(student_tmp) +'''
                    </p>
                    <h3>
                        Items ordered :
                    </h3>
                    <p>
                    '''+ str(orders_list) +'''
                    </p>
                </body>
            </html>'''
                f.write(message)

        another_student = input('Do you want to take other orders from other students? (Type "Yes" to confirm): ').strip().title()
    
'''student_tmp['sWal'] = student_tmp['sWal'] - price_amount'''
print(studentList)
print('Total amount the store has earned: Php ' + str(round(total_store_profit, 2)))

print(menu_qty)

with open(file_name,'a') as f:
    message = '''
<html>
    <body>
        
        <h2>
        Total Store Profit :
        </h2>
        <p>
        Php '''+ str(total_store_profit) +'''
        </p>
    </body>
</html>'''
    f.write(message)

webbrowser.open_new_tab(file_name)

''' Total Number of Quantity '''
''' Total Price Amount '''
