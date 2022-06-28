class User():
    def __init__(self, first_name, last_name, nickname, email, birthday):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.nickname = nickname
        self.email = email
        self.birthday = birthday.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  nickname: " + self.nickname)
        print("  Email: " + self.email)
        print("  birthday: " + self.birthday)

    def greet_user(self):
        print("\nWelcome back, " + self.nickname + "!" + "Hisashiburidesu!")
    
Maricel = User('Maricel', 'Ranes', 'Cel', 'Maricel_Sabando@yahoo.com', 'June 05')
Maricel.describe_user()
Maricel.greet_user()

Mechelle = User('Mechelle', 'Aranez', 'Mayan', 'Mayan_Aranez@yahoo.com', 'March 04')
Mechelle.describe_user()
Mechelle.greet_user()
