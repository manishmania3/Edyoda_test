def addition(x,y):
	return x+y
def subtraction(x,y):
	return x-y
def multiplication(x,y):
	return x*y
def truedivision(x,y):
	return x/y
def divide(x,y):
	return x//y,x%y
if __name__ == '__main__':
	a = 10
	b = 3
	print(addition(a,b))
	print(subtraction(a,b))
	print(multiplication(a,b))
	print(truedivision(a,b))
	print(divide(a,b))