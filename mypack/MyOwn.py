class Human:

    def __init__(self):
        pass

    def printi(self):
        self.name = input("Your name:")
        self.age = input("Your Age:")
        self.validateAge()
        self.mobile = input("Your Mobile number:")

    def validateAge(self):
        if self.age < 18:
            print("Your not under 18")
            exit()
