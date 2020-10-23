def square(x):
	return x*x
def cube(x):
	return x*x*x
def custom(x,y):
	return x**y
if __name__ == '__main__':
	a = 2
	b = 10
	print(square(a))
	print(cube(a))
	print(custom(a,b))