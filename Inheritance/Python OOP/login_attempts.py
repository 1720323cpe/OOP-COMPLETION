class User():
    def __init__(self, first_name, last_name, nickname, email, birthday):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.nickname = nickname
        self.email = email
        self.birthday = birthday.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  nickname: " + self.nickname)
        print("  Email: " + self.email)
        print("  birthday: " + self.birthday)

    def greet_user(self):
        print("\nWelcome back, " + self.nickname + "!" + "Hisashiburidesu!")

def increment_login_attempts(self):
        self.login_attempts += 1

def reset_login_attempts(self):
        self.login_attempts = 0

Maricel = User('Maricel', 'Ranes', 'Cel', 'Maricel_Ranes@yahoo.com', 'June 05')
Maricel.describe_user()
Maricel.greet_user()

print("\nMaking 3 login attempts...")
Maricel.increment_login_attempts()
Maricel.increment_login_attempts()
Maricel.increment_login_attempts()
print("  Login attempts: " + str(Maricel.login_attempts))
print("Resetting login attempts...")
reset_login_attempts()
print("  Login attempts: " + str(Maricel.login_attempts))