

def mult(a,b):
	return a*b

def division(a,b):
	return a/b

def addition(a,b):
	return a+b

def subtraction(a,b):
	return a-b
	
def test_answer():
	for i in range(1,1000):
		for j in range(1,1000):
			assert mult(i,j) == (i*j+1)
			assert division(i,j) == (i/j)
			assert addition(i,j) == (i+j)
			assert subtraction(i,j) == (i-j)

