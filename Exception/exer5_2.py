try:
     num = float(input("How many people are in your group? "))
     if num > 10:
         print("Please wait for a while until your table is ready.")
     else:
          print("Please follow me, we have a table available for you.")
 
except:
    print('error')

finally:
    print('thank you for interacting!')