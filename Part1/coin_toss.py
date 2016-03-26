from random import randint


def coin_toss():

	flips = 0

	# messages
	trials_msg = "\nHow many trials do you want to run? "
	val_err_msg = "That is not a valid number of trials. Please try again..."
	flips_msg = "The average number of flips is: "

	# user input to determine number of trials
	while True:
		
		try:
			trials = int(input(trials_msg))
			break
	
		except ValueError:
			print(val_err_msg)

	
	# run simulation
	for i in range(1, trials + 1):
		
		first_flip = randint(0,1) # determine first flip value
		flips += 1 # accounts for first_flip

		# determine if subsequent flip is the same as first_flip
		while randint(0,1) == first_flip:
			flips += 1 
		else:
			flips += 1 # accounts for flip different than first_flip

	# calculates the average number of flips
	flip_avg = round(flips / trials, 2)

	print(flips_msg + "{}".format(flip_avg))


if __name__ == "__main__":
	coin_toss()