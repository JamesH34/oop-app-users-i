class User:

    def __init__(self, name, email, username, drivers_license):
        self.name = name 
        self.email = email
        self.username = username
        self.drivers_license = drivers_license

    def __str__(self):
        return f"I am {self.name} my email is {self.email} my username is {self.username} and drivers_license is {self.drivers_license}."

    def password(self, secret_code):
        print(f"{self.name}'s password is {secret_code}")




john = User("John", "john@gmail.com", "John123", "123456")
kevin = User("kevin", "kevin@gmail.com", "kevin123", "1098765")
kevin.password("12345")
john.password("password789")
print(john)
print(kevin)
