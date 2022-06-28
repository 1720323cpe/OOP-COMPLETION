try:
     dinnerparty_number = input("How many people are in your dinner party tonight? ")
     dinnerparty_number =int(dinnerparty_number)

     if dinnerparty_number > 10:
         print("I'm sorry, you'll have to wait for a table.")
     else:
         print("Your table is ready.")
  
except:
    print('error')

finally:
    print('thank you for interacting!')