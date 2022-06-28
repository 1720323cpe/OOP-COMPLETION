#RANES, ALTHEA LIEZL S.
#CPE2A
def studentsdata():
    try:
        Studname_323 = input("Enter Name: ")
        Id = int(input("\nID: "))
        year = input("\nYear: ")
        course_section = input("\nCourse and Section: ")
    except:
        print("Invalid Input")
        return studentsdata()
    
    student_info = {
        'Name': Studname_323,
        'ID': Id, 
        'year':year,
        'course':course_section,
        'Initial amount of money': 150
    }
    
    print("\nMay I check your information please.\n")
    print("Course and Section: "+ student_info['course'])
    print('\nStudent Name: '+student_info['Name'])
    print('\nID: '+ str(student_info['ID']))
    print('\nYear: '+ student_info['year'])
    
    deci = input("Would you like to change your informations? (Yes or No)").lower()
    if deci == 'yes':
        return studentsdata()
    
    print('OK.\n\n')
    
    print('You have 150php worth of money\n\n')


studentsdata()       

def price():
    drinks = {'4 Soda','4 Bottled Water','2 Coffee','2 Tea'}
    snacks = {'1 Bread','5 Apple','5 Banana','3 Oranges'}
    meals = {'5 Tapsilog','4 Porksilog'}
    DrinkPrice = {29.25,20,50,35.50}
    SnackPrice = {15, 20.50, 15,25.10}
    MealPrice = {80.99,80.99}
    
    drinknumitems = {4,4,2,2}
    snacknumitems = {1,5,5,3}
    mealnumitems = {5,4}

    i1=0
    i2=0
    i3=0
    i4=0
    i5=0
    i6=0
    
    IAV_money = 150
    total = 0
    change = 0
    print("Lists of drinks and their price.\n")
    
    for b in drinks:
        i1+=1
        print('drink number '+str(i1) +": "+b)
    
    print('\n')
    for a in DrinkPrice:
        i2+=1
        print('drink number '+str(i2)+": "+str(a))
        
    print("\n List of snacks and their price. \n")
    for c in snacks:
        i3+=1
        print('snack number '+str(i3) +": "+c)
    
    print('\n')
    for d in SnackPrice:
        i4+=1
        print('snack number '+str(i4)+": "+str(d))
    
    print ("\nLists of meals and their price.\n")
    for e in meals:
        i5+=1
        print('drink number '+str(i5) +": "+e)
    
    print('\n')
    for f in MealPrice:
        i6+=1
        print('drink number '+str(i6)+": "+str(f))
    
    print('\n\n\nD1: Soda 29.25php\n D2: Bottled Water 20php\nD3: Coffee 50php\nD4: Tea 35.50php')

    print('S1: Bread 15php\n S2: Appler 20.50php\nS3: Banana 15php\nS4: Orange 25.10php')

    print('M1: Tapsilog 80.99php\nM2: Porksilog 80.99php\n\n\n')

    while (1):
        pick = input('Type \nD1-D4(Drinks 1-4, \nS1-S4 (Snacks 1-4), \nM1-M2(Meal 1-2)\nto order an item\n\nType CONFIRM to confirm purchase\nType EXIT to cancel order').upper()

        if pick=='EXIT':
            print('\nOkay have a nice day')
            quit()
        elif pick == 'CONFIRM':
            print('Total amount: ',total)
            change = IAV_money - total
            if change < 0:
                print('insufficient funds')
                print('Your balance is ',IAV_money)
                print('You need ',change,' more')
                quit()
            else:
                print('Your balance is ',IAV_money)
                print('Your change is ',IAV_money)
                print('\n\nCome Again!')
                quit()
        elif pick == 'D1':
            d = int(input('How many SODA?'))
            if d > 4:
                print('Remaining:4')
               
            else:
                total = total + 29.25 * d
        elif pick == 'D2':
            d = int(input('How many BOTTLED WATER?'))
            if d > 4:
                print('Remaining:4')
                
            else:
                total = total + 20 * d
        elif pick == 'D3':
            d = int(input('How many COFFEE?'))
            if d > 2:
                print('Remaining:2')
                
            else:
                total = total + 50 * d
        elif pick == 'D4':
            d = int(input('How many TEA would you like to have?'))
            if d > 2:
                print('Remaining:2')
            else:
                total = total + 30.50 * d
        elif pick == 'S1':
            d = int(input('How many BREAD would you like to have?'))
            if d > 1:
                print('Remaining:1')
            else:
                total = total + 15 * d
        elif pick == 'S2':
            d = int(input('How many APPLE would you like to have?'))
            if d > 5:
                print('Remaining:5')
            else:
                total = total + 20.50 * d
        elif pick == 'S3':
            d = int(input('How many BANANA would you like to have?'))
            if d > 5:
                print('Remaining:5')
            else:
                total = total + 15 * d
        elif pick == 'S4':
            d = int(input('How many ORANGES would you like to have?'))
            if d > 3:
                print('Remaining:3')
            else:
                total = total + 25.10 * d
        elif pick == 'M1':
            d = int(input('How many servings of TAPSILOG?'))
            if d > 5:
                print('Remaining:4')
            else:
                total = total + 80.99 * d
        elif pick == 'M2':
            d = int(input('How many servings of PORKSILOG?'))
            if d > 4:
                print('Remaining:44')
            else:
                total = total + 80.99 * d
        else:
            print('Your Input is Invalid')
price()   
