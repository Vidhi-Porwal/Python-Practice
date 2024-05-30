""" write a python scrip to take order from user by displaying specific menu items"""
"""if else ladder"""
print ("Hi, here is our menu.")
print ("1: Tea")
print ("2: Coffee")
print ("3: Soup")
print ("4: Soda")
print ("5: Water")
order=int(input("enter no. of your order:"))
if (order== 1):
	print("Tea is ready")
elif (order==2):
	print("Coffee is ready")
elif (order==3):
	print("Soup is ready")
elif (order==4):
	print("Soda is ready")
elif (order==5):
	print("Water is ready")
else:
	print("Invalid item choice")

