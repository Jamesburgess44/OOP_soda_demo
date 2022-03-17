from soda import Soda
from vending_machine import VendingMachine

soda_one = Soda("Coke")
soda_two = Soda("Pepsi")

print(soda_one.ammount_of_soda)
soda_one.Open_soda()
soda_one.take_drink()
print(soda_one.ammount_of_soda)


vending = VendingMachine()
vending.load_soda(soda_two)
vending.load_first_soda(vending.first_soda)
vending.what_is_in_machine()
print(soda_two.name)