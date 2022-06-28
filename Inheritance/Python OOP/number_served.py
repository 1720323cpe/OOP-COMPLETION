class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " serves you a very delicious " + self.cuisine_type + "called Adepti Temptation"
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " Welcomes you. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restaurant('Monstandt X Liyue', 'soup')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 304
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(430)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(605)
print("Number served: " + str(restaurant.number_served))
