import sys

def mul(a,b):
	x = a * b
	return x

def main():
	if (len(sys.argv) > 3):
		print("Erreur, il y a plus de deux arguments")
	elif (len(sys.argv) == 1):
		print("Erreur, il manque" , (3 - (len(sys.argv))) , "arguments")
		x = int(input("Entrez le premier argument: "))
		y = int(input("Entrez le deuxieme argument: "))
		print(mul(int(x),int(y)))
	elif (len(sys.argv) == 2):
		print("Erreur, il manque" , (3 - (len(sys.argv))) , "arguments")
		y = int(input("Entrez le deuxieme arguments: "))
		x = sys.argv[1]
		print(mul(int(x),int(y)))
	else:
		x = sys.argv[1]
		y = sys.argv[2]
		print(mul(int(x),int(y)))

main()
