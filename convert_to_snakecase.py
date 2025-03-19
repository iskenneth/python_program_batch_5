#Ask the user to input their full name.
fullname = input("Enter your full name: ")
#Convert all letters to lowercase.
words = fullname.lower().split()
#Replace spaces with underscores.
snake_case= '_'.join(words)
#Print the result.
print ("Output", snake_case)