#Exercise 2
try:
    def make_shirt(size='large', message='Mathew 6:33'):
        print("\nI'm going to make a " + size + " t-shirt.")
        print('It will say, "' + message + '"')

    make_shirt()
    make_shirt(size='medium')
    make_shirt('small', 'DREAM BIG!.')

except:
    print('Error!.')
finally:
    print('\nThank you for using this program')