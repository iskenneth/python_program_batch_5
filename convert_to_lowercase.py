#Ask the user to input their full name.
while True:
    try:
        pagkakakilanlan = input("Enter your full name: ")
    except ValueError:
        print("..............")
#Convert all letters to lowercase.
#Print the result.