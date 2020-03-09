import sys

def mul(a,b):
	x = a * b
	return x

def main():
	if (len(sys.argv) > 3):
		print("Erreur, il y a plus de deux arguments")
	elif (len(sys.argv) < 3):
		print("Erreur, il y a moins de deux arguments")
	else:
		x = sys.argv[1]
		y = sys.argv[2]
		print(mul(int(x),int(y)))

main()
