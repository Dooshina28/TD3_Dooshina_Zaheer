import sys

def add(a,b):
	x = a + b
	return x

def main():
	if (len(sys.argv) > 3):
		print("Erreur, plus de deux arguments")
		sys.exit(1)
	elif (len(sys.argv) < 3):
		print("Erreur, moins de deux arguments")
		sys.exit(1)
	else:
		x = sys.argv[1]
		y = sys.argv[2]
		print(add(int(x),int(y)))

main()

