#Ask the user to input a sentence.
while True:
    try:
        sentence = input("Enter a statement: ")
        word_in_sentence = len(sentence.split())#Count the number of words.
    except ValueError:
        print("ERROR!!!")

#Print the result.
