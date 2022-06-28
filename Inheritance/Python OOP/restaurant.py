class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + " serves you a very delicious " + self.cuisine_type + " called Adeptus Temptation"
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " Welcomes you. Come on in!"
        print("\n" + msg)

restaurant = Restaurant('Monstandt X Liyue', 'soup')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()