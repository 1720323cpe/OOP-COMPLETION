prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        active = False
        print("Thank you For stopping by!")
        break
    if age == 'no':
        break
    if age == " ":
        continue
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 12:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")