
import string
import random
# check to get int length of othe password
def get_integer(x):
    while True:
        user_input = input(x)
        try:
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Invalid input. Please enter an integer.")

integer_len = get_integer("Enter an integer:")
print(f"You entered: {integer_len}")


print('''Choose character set for password from these :
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

characterList = ""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):

		# Adding letters to possible characters
		characterList += string.ascii_letters
	elif(choice == 2):

		# Adding digits to possible characters
		characterList += string.digits
	elif(choice == 3):

		# Adding special characters to possible
		# characters
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []
list_character=list(characterList)
random.shuffle(list_character)
password=list_character[:integer_len]

# printing password as a string
print("The random password is " + "".join(password))
