#program using simple calsy
i=int(input("enter the value of i:"))
j=int(input("enter the value of j:"))
o=input("what do you want to do? +,-,*,/:")

def add():
	return i+j
def sub(a,b):
	return a-b
def mult(a,b):
	return a*b
def divide(a,b):
	return a/b

if(o=='+'):
	print("addition=",add())
elif(o=='-'):
	print("subtraction=",sub(i,j))
elif(o=='*'):
	print("multiplication=",res)
elif(o=='/'):
	print("division=",divide(i,j))		