# python learning exercises

# Functions
def echo(thing):
	return thing

def swap(thunder, chocolate):
	return chocolate, thunder
	
def main_function():
	print "testing echo('marco'): ", echo('polo')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('thunder', 'chocolate')", swap('thunder', 'chocolate')
	


#Arithmetic Functions
def reverse(x):
	return -x
	
def plus(a,b):
	return a+b

def diff(x,y):
	return x-y

def abs_diff(d,b):

def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "test add (7,5): ", plus(7,5)
	print "test diff (50,20): ", diff(50,20)




def main():
	main_function()
	main_arithmetic()
	
main()
