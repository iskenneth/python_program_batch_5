#Ask the user to input their full name.
while True:
    try:
        name = input("Enter your Full name: ")
    except ValueError:
        print("ERROR!!")
#Convert all words to lowercase.
#Capitalize the first letter of each word.
#Remove spaces between words.
#Print the result