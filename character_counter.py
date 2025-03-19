#Ask the user to input their full name.
while True:
    try:
        pangalan = input("Enter your Full name:")
    except ValueError:
        print("Wrong character")
#Count the total number of characters, including spaces.
#Print the result.