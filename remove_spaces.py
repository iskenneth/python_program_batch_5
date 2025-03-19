#Ask the user to input their full name with spaces.
while True:
    try:
        fullname = input ("Enter your Full Name WITH SPACES: ")
    except ValueError:
        print("Error 404!!")
#Remove spaces at the beginning.
#Print the result.