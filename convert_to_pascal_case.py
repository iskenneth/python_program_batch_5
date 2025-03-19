#Ask the user to input their full name.
while True:
    try:
        name = input("Enter your Full name: ")
        words = name.lower().split() #convert input to lower case 
        pascal_case = ''.join(word.capitalize () for word in words) #convert to pascal case
        print ("Output: ", pascal_case)
        break
    except ValueError:
        print("ERROR!!")

