#Exercise 5
try:
    def show_magicians(magicians):
        for magician in magicians:
            print(magician.title())

    magicians = ['Chris Angel', 'Michael Carbonaro', 'Dynamo']
    show_magicians(magicians)

except:
    print('Error!.')
finally:
    print('\nThank you for using this program')