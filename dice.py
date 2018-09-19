#write a program of dice with random numbers
import random

while True:
	x=input("enter 'r'to roll a die and 'q'to quit")
	if(x=='r'):
		print(random.randint(1,6))
	elif(x=='q'):
		print("completed")
		break
	else:
		print("give either'r'or'q'")		
		
 