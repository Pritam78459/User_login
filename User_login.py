import json

def acc_creation():
	name = input('Enter name:')
	password = input("Create password:")

	file_name1 = 'name.json'
	file_name2 = 'pass.json'
	with open(file_name1, 'w') as l_objects:
		json.dump(name, l_objects)
	with open(file_name2, 'w') as l_objects:
		json.dump(password, l_objects)
	print("we'll remember you next time!")

def acc_login():
	file_name1 = 'name.json'
	with open(file_name1) as f_objects:
		name = json.load(f_objects)
	file_name2 = 'pass.json'
	with open(file_name2) as f_objects:
		password = json.load(f_objects)
	while True:
		name1 = input("Enter your name = ")
		password1 = input("Enter password = ")
		if name1 == name:
			print("Welcome back " + name + '!')
		if password1 == password:
			print("Password is correct")
			break
		else:
			print('password is incorrect')

print("Would you like to create an account or log in?")
choice1 =  input("To create a account enter y and to log in enter n:[y/n]")
if choice1 == 'y':
	acc_creation()
else:
	acc_login()