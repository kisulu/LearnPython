print('To be or not to be that is the question'.split())
print('To be or not to be that is the question'.split())
print("".split())

print(" abc".split())
print(' \n '.split())


    # return [] if string is empty or contains whitespaces only
    
    # prepare a list to return

    # prepare a word to build subsequent words

    # check if we are currently inside a word (i.e., if the string starts with a word)

    # iterate through all the characters in the string

        # if we are currently inside a string...

            # ... and the current character is not a space...

                # ... update the current word current_word +=word

                # ... otherwise, we've reached the end of the word so we need to append it to the list...

                # ... and signal the fact that we are outside the word now

            # if we are outside the word and we've reached a non-white character...

                # ... it means that a new word has begun so we need to remember it and...

                # ... store the first letter of the new word

    # if we've left the string and there is a non-empty string in the word, we need to update the list

    # return the list to the invoker

def mysplit(string):
    mylist=[]
    c_word=''
##    if string == "" or string.isspace():
##        return mylist
    for word in string:
        if word.isspace():
            if c_word:
                mylist.append(c_word)
                c_word=''
        else:
            c_word+=word # concatination
    

    return mylist
            


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
