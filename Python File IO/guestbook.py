
ranes_althea = 'guest_book.csv'

print("Enter 'exit' when you are finished.")

while True:
    name = input("\nWhat's your name? ")
    date = input("Enter the date today to register (Y/M/D")
    if name == 'exit':
        break
    else:
        with open(ranes_althea, 'a') as f:
            f.write(name + "\n")
            f.write(date + "\n")
        print("Hi " + name + ", you've been added to the guest book.")
        print("You regestered at" + date)
