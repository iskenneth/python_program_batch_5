#Ask the user to input their full name.
while True:
    try:
        full_name = input("Enter your Full name:")
    except ValueError:
        print("ErR0r 404!!")
#Capitalize the first letter of each word.
#Print the result.