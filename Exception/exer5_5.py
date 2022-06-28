try:
     prompt = "\nWhat topping would you like on your pizza?"
     prompt += "\nEnter 'quit' when you are finished: "
     while True:
         topping = input(prompt)
     if topping != 'quit':
         print("  I'll add " + topping + " to your pizza.")
     else:
         print ('edible toppings only')
  
except:
    print('error')

finally:
    print('thank you for interacting!')