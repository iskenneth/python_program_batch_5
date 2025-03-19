#Ask the user to input their full name
while True:
    try:
        pangalan = input("Enter your Full name (in any casing you want: ")
        #Print the result.
        print("Output: ", pangalan.swapcase())#Change uppercase letters to lowercase and vice versa.
    except ValueError:
        print("hindi pwede yan ngaaaa!!!!")