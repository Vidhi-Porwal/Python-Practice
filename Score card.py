"""write a python programe to implement the given below rubric on given below score
exactly 100: 5star
b/w 100-70 : 4star
b/w 70-60 : 3star
b/w 60-50 : 2star
below 50 : 1star"""
print("""SCORE CARD
	exactly 100: 5star
	b/w 100-70 : 4star
	b/w 70-60 : 3star
	b/w 60-50 : 2star
	below 50 : 1star""")
score=int(input("enter no. of your Score:"))
if (score== 100):
	print("4 Star and Perfect")
elif (score<100) and (score>=70):
	print("4 Star")
elif (score<70) and (score>=60):
	print("3 Star")
elif (score<60) and (score>=50):
	print("2 Star")
elif (score<50) :
	print("1 star")
else:
	print("Invalid Score")
