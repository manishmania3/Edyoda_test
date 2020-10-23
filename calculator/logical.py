def andgate(x,y):
	return x and y
def orgate(x,y):
	return x or y
def notgate(x):
	return not x
def nandgate(x,y):
	return not andgate(x,y)
def norgate(x,y):
	return not orgate(x,y)
def xorgate(x,y):
	return nandgate(x,y) and orgate(x,y)
if __name__ == '__main__':
	a = True
	b = False
	print(andgate(a,b))
	print(orgate(a,b))
	print(notgate(a),notgate(b))
	print(nandgate(a,b))
	print(norgate(a,b))
	print(xorgate(a,b))