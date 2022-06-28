#Exercise 1
try:
    def make_shirt(size, message):
        print("\nI'm going to make a " + size + " t-shirt.")
        print('It will say, "' + message + '"')

    make_shirt('large', 'TATAKAE')
    make_shirt(message="Shizou wo SASAGEYO", size='large')

except:
    print('Error!.')
finally:
    print('\nThank you for using this program')