"""
    In this problem you will open a file (four.txt), you will read some information from the file
    then you will right a output of that information to a new file solution4.txt
    1) On every line of the file input there is a character that is uppper or lower when
    the other characters are the opposite
    Concatenate all of these characters to build a message.
    2) Sum all of the numbers on the first 10 lines, call this final number J
       Split the 11th line on the most frequent character
       the word at the Jth position can be called the Fword
       Return the number of times that the Fword appears in the file case insensitive.
    3) In solution4.txt output on the first line the message, the next line the frequency
    Example solution4.txt:
    "Hidden Message"
    34

"""

#Hidden Message found
def fun():
    with open (four.txt) as fin:
    for line in fin:
       for achar in line:
        if achar.isupper():
            message += achar
    return message
    

if __name__ == "__main__":
    print(fun())
