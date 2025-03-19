#Ask the user to input their full name.
while True:
    try:
        pagkakakilanlan = input("Enter your full name: ")
        #Print the result.
        print ("Output: ", pagkakakilanlan.lower())            
    except ValueError:
        print("..............")