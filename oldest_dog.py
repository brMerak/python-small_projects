my_dogs = []
oldest_dogs = []

def add_dog():
	while True:
		question = input("Want to add a new dog to the list?\nType 'y' or 'yes'\n>").lower()
		if question == 'y' or question == 'yes':
			dog_name = input("Please enter the name of your dog:\n>").title()
			if dog_name == '' or dog_name == int:
				print("That is not a valid name")
				break
			dog_age = input("Please enter the age of your dog:\n>")
			if dog_age == '':
				dog_age = 0
			my_dogs.append((dog_name, int(dog_age)))
			
		else:
			print("The list is complete.")
			break
	if len(my_dogs) > 1:
		print(my_dogs)

def oldest_one():
	x = sorted(my_dogs, key = lambda x: x[1])[::-1]

	for i in range(len(x)):
		if x[0][1] == x[i][1]:
			oldest_dogs.append(x[i][0])
	
	if len(oldest_dogs) > 1:
		print(f"You have {len(oldest_dogs)} dogs that are {x[0][1]} years old:")
		for i in oldest_dogs:
			print(i)
	else:
		print(f"Your oldest dog is {oldest_dogs[0]} and it is {x[0][1]} years old.")

add_dog()
oldest_one()


