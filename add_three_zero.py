#Ask the user to input a number (0-1000).
while True:
    try:
        number = int(input("Enter a numner from 1-1000:"))
        #Print the result.
        print ("Output:", f"{number : 06d}") #Add leading zeros to make it 6 digits.
        break
    except ValuerError:
        print ("79&7$+#;_('+;$*)")

