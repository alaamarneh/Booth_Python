class Register:
    def __init__(self, name, value='0'):
        self.name = name
        self.value = value

    def print_value(self):
        print("Register " + self.name + " = " + str(self.value))
