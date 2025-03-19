#Ask the user to input their full name.
while True:
    try:
        pangalan = input("Enter your full name: ")
    except ValueError:
        print("ERROR 404!!!")
#Convert all letters to uppercase.
#Print the result.