import sys

def add(a,b):
	x = a + b
	return x

def main():
	x = sys.argv[1]
	y = sys.argv[2]
	print(add(int(x),int(y)))

main()

