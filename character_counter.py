#Ask the user to input their full name.
while True:
    try:
        pangalan = input("Enter your Full name:")
        #Print the result.
        print("Count: ", len(pangalan)) #Count the total number of characters, including spaces.
        break
    except ValueError:
        print("Wrong character")