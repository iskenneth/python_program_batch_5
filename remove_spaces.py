#Ask the user to input their full name with spaces.
while True:
    try:
        fullname = input ("Enter your Full Name WITH SPACES:")
        #Print the result.
        print("Output:" , fullname.lstrip())#Remove spaces at the beginning.
    except ValueError:
        print("Error 404!!")

