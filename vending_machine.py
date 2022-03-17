from soda import Soda

class VendingMachine:
    def __init__(self):
        self.storage = []
        self.first_soda = Soda("Mountain Dew")


    def load_soda(self, soda_object):
        self.storage.append(soda_object)
        print(f'{soda_object.name} has been added to the vending machine')

    def load_first_soda(self, included_soda):
        self.storage.append(included_soda)
        print(f'{included_soda.name} has been added to the vending matchine')

    def what_is_in_machine(self):
        for soda in self.storage:
            print(soda.name)