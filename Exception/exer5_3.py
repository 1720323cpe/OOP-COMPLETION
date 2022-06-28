try:
     number = input("enter a number100: ")
     number = int(number)

     if number % 10 == 0:
          print(str(number) + " is a multiple of 10.")
     else:
          print(str(number) + " is not a multiple of 10.")
  
except:
    print('error')

finally:
    print('thank you for interacting!')