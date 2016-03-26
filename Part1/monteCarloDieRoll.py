from random import randint


def monte_carlo_sim():
	
	total = 0

	while True:
		try:
			sim = int(input("Enter the number of simulations to test: "))
			break
		except ValueError:
			print("That is not an integer. Please try again...\n")

	for i in range(1, sim + 1):
		roll = randint(1,6)
		total += roll
	
	print("\nThe average of {:,} die rolls is {}\n".format(i, round(total / i, 3)))


if __name__ == "__main__":
	monte_carlo_sim()
