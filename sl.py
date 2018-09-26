#write a program of a game snake and ladder
import random
count=0
def myroll():
	return random.randint(1,6)

while(count<=100):
	n=input("press r to roll the dice")
	if(n=='r'):
		r=myroll()
		count=count+r
		print("u got ",r)
		print("new position is",count)

		if (count==8):
			count=7
			print("u got the lader")
		elif(count=11):
			count=2
			print("sorry,u got snake")
		elif(count=13):
			count=34
			print("u got the ladder")
		elif(count=25):
			count=4
			print("sorry,u got snake")
		elif(count=38):
			count=9
			print("sorry,u got snake")
		elif(count=40):
			count=68
			print("u got the ladder")
		elif(count=52):
			count=81
			print("u got the ladder")
		elif(count=65):
			count=46
			print("sorry,u got snake")
		elif(count=76):
			count=97
			print("u got the ladder")
		elif(count=89):
			count=70
			print("sorry,u got snake")
		elif(count=93):
			count=64
			print("sorry,u got snake")
			