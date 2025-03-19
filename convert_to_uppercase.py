#Ask the user to input their full name.
while True:
    try:
        pangalan = input("Enter your full name: ")
        #Print the result.
        print("Output: ", pangalan.upper()) #Convert all letters to uppercase
        break
    except ValueError:
        print("ERROR 404!!!")