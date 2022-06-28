#Exercise 6
try:
    def show_magicians(magicians):
        for magician in magicians:
            print(magician)

    def make_great(magicians):
        great_magicians = []

        while magicians:
            magician = magicians.pop()
            great_magician = magician + ' the GOAT'
            great_magicians.append(great_magician)

        for great_magician in great_magicians:
            magicians.append(great_magician)

    magicians = ['Chris Angel', 'Michael Carbonaro', 'Dynamo']
    show_magicians(magicians)

    print("\n")
    make_great(magicians)
    show_magicians(magicians)

except:
    print('Error!.')
finally:
    print('\nThank you for using this program')