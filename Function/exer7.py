#Exercise 7
try:
    def make_sandwich(*items):
        print("\nI'll make you a great sandwich:")
        for item in items:
            print("  ...adding " + item + " to your sandwich.")
        print("Your sandwich is ready!")

    make_sandwich('mayionise', 'bacon', 'lettuce', 'egg')
    make_sandwich('nuttela', 'a slice of banana')
    make_sandwich('strawberry jam')

except:
    print('Error!.')
finally:
    print('\nThank you for using this program')