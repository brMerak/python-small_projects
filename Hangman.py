from random import randint

word = ["hello", "bottle", "candy", "telephone", "keyboard"]
word = list(word[randint(0,(len(word)-1))].upper())
board = list('_' * len(word))
guessed_letters = []

def start_game():
	print("Lets play a game of Hangman.")
	print("Ready? Let's go!")	
	hangman()
	
	
def hangman():
	guess = 10
	
	while guess >= 0:
		if ''.join(board).lower() == ''.join(word).lower():
			print(f"\nYou have guessed the word correctly: {''.join(word)}")
			break
		my_guess = input(f"\nGuess a letter: (you have {guess} guesses left)\n>").upper()
		if len(my_guess) == 1:
			if my_guess in word:
				if my_guess not in board:
					guessed_letters.append(my_guess)
					for i in range(len(word)):
						if word[i] == my_guess:
							board[i] = my_guess
					guess -= 1
					print("\nThe word is:")
					print(board)
					print("\nYour guesses:")
					print(guessed_letters)
				
				else:
					print("\nYou have guessed this letter already. Try again.")
								
			elif my_guess not in word:
				if my_guess not in guessed_letters:
					guessed_letters.append(my_guess)
					print("\nThe word is:")
					print(board)
					print("\nYour guesses:")
					print(guessed_letters)
					guess -= 1
				
				else:
					print("\nYou have tried that letter already. Please try again.")
					print("\nThe word is:")
					print(board)
					print("\nYour guesses:")
					print(guessed_letters)
		else:
			print("\nYou cannot guess more than one letter at a time. Try again.")

	if guess == 0 and ''.join(board).lower() != ''.join(word).lower():
		print("You have run out of guesses and have been hanged.")

start_game()