from random import random


def election_outcome():
	
	# Candidate A's chance of winning by region
	region_1 = .87
	region_2 = .65
	region_3 = .17

	
	# messages
	default_num_of_trials = "\nDo you want to run 100,000 trial elections? "
	num_of_trials = "\nHow many trial elections do you want to run? "
	val_err_message = "That is not a valid integer. Please try again..."
	
	A_prob_message = "\nThe probability of candidate A winning is: "
	B_prob_message = "The probability of candidate B winning is: "
	
	A_wins_message = "Candidate A wins!!!\n"
	B_wins_message = "Candidate B wins!!!\n"

	A_total_wins = 0
	B_total_wins = 0


	while True:
		
		answer = input(default_num_of_trials)

		try:
			if answer.lower() == 'yes' or answer.lower() == 'y':
				trials = 100000
				break
			else:
				trials = int(input(num_of_trials))
				break

		except ValueError:
			print(val_err_message)


	for trial in range(1, trials + 1):
		
		A_win = 0
		B_win = 0
		
		if random() < region_1: # 1st region
			A_win += 1
		else:
			B_win += 1

		if random() < region_2: # 2nd region
			A_win += 1
		else:
			B_win += 1

		if random() < region_3: # 3rd region
			A_win += 1
		else:
			B_win += 1

		
		if A_win > B_win: # overall election outcome
			A_total_wins += 1
		else:
			B_total_wins += 1

	
	A_probability = round(A_total_wins / trials * 100, 2)
	B_probability = round(B_total_wins / trials * 100, 2)

	
	print(A_prob_message + "{}%".format(A_probability))
	print(B_prob_message + "{}%\n".format(B_probability))

	
	if A_probability > B_probability:
		print(A_wins_message, end="\n")
	else:
		print(B_wins_message, end="\n")


if __name__ == "__main__":
	election_outcome()	