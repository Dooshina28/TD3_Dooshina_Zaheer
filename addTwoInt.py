import sys

def add(a,b):
	x = a + b
	return x

def main():
	if (len(sys.argv) > 3):
		print("Erreur, il y a", ((len(sys.argv)) - 3), " plus de arguments")
		sys.exit(1)
	elif (len(sys.argv) == 1):
		print("Erreur, il manque ", (3 - (len(sys.argv))), "  arguments")
		x = int(input("Entrez la valeur du premier argument: "))
		y = int(input("Entrez la valeur du deuxieme argument: "))
		print(add(int(x),int(y)))
	elif (len(sys.argv) == 2):
		print("Erreur, il manque", (3 - (len(sys.argv))), "  arguments")
		y = int(input("Entrez la valeur du deuxieme argument: "))
		print(add(int(sys.argv[1]),int(y)))
	else:
		x = sys.argv[1]
		y = sys.argv[2]
		print(add(int(x),int(y)))

main()

