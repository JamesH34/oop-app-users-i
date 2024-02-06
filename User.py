class User:

    def __init__(self, name, email, username, password):
        self.name = name 
        self.email = email
        self.username = username
        self.password = password

    def __str__(self):
        return f"I am {self.name} my email is {self.email} my username is {self.username} and password is {self.password}."

john = User("John", "john@gmail.com", "John123", "John's-password")
kevin = User("kevin", "kevin@gmail.com", "kevin123", "kevin's-password")
print(john)
print(kevin)