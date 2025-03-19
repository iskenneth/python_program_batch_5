#Ask the user to input their full name
while True:
    try:
        pangalan = input("Enter your Full name (in any casing you want: ")
    except ValueError:
        print("hindi pwede yan ngaaaa!!!!")
#Change uppercase letters to lowercase and vice versa.
#Print the result.