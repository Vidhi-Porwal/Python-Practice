"""write python script to identify highest number form 3 user defined integers"""


var_a= float(input("Enter Value 1: "))
var_b= float(input("Enter Value 2: "))
var_c= float(input("Enter Value 3: "))
"""if(var_a>var_b):
	var_d=var_a
else:
	var_d=var_b
if(var_c>var_d):
	print(var_c)
else:
	print(var_d)"""
"""if (var_a>var_b) and (var_a>var_c):
	print("{}is greatest".format(var_a))
elif(var_b>var_a) and (var_b>var_c):
	print("{}is greatest".format(var_b))
else:
	print("{}is greatest".format(var_c))"""
if (var_a>=var_b) and (var_a>=var_c):
	print("{}is greatest".format(var_a))
elif(var_b>=var_a) and (var_b>=var_c):
	print("{}is greatest".format(var_b))
else:
	print("{}is greatest".format(var_c))