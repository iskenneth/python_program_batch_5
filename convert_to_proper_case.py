#Ask the user to input their full name.
while True:
    try:
        full_name = input("Enter your Full name:")
        #Print the result.
        print("Output: ", full_name.title()) #Capitalize the first letter of each word.
        break
    except ValueError:
        print("ErR0r 404!!")