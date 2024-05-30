"""x= int(input("Enter temp(in °C): "))
if (x>20):
	print("Lime Water")
elif (x<10):
	print("Hot Chocolate")
elif (x>=15) and (x<=18):
	print("coffee")
else:
	print("Tea")"""
"""else (x<15) and (x==19) and (x==20):
	print("Tea")"""

x= float(input("Enter temp(in °C): "))
if (x>20):
	print("Lime Water")
elif (x>=10) and (x<=20):
	if (x>=15) and (x<=18):
		print("coffee")
	else:
		print("Tea")
elif(x<10):
	print("Hot Chocolate")