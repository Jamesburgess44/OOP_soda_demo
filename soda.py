class Soda:
    def __init__(self, name):
        self.name = name
        self.is_open = False
        self.ammount_of_soda = 100
    
    def Open_soda(self):
        self.is_open = True
        print("you have opened the can of soda, try taking a drink")

    def take_drink(self):
        if self.is_open == True:
            self.ammount_of_soda = self.ammount_of_soda - 10
            print("you take a swig of the soda")
        else:
            print("you cant take a drink until you have opened the soda")
    