list_sent = ["hello world","I love Python"]
o_dict = {}

for sent in list_sent:
    """ print(sent) print each sentence 0 , 1"""
    for letter in sent:
        """print(l) prints letters """
        if letter.isalpha():
            """checks if it is alphabet"""
            if letter in o_dict.keys():
                """Take the letters and make them keys of the dictionary
                    which are always unique ie dict["a"]=1 as value"""
                ## if letter exist in dict then increment
                o_dict[letter] +=1
                ## print(o_dict) avoid this since it prints many times arccording to loop
                ## we print outside the loop
            else:
                """else make the value of the letter in the dictionary 1"""
                o_dict[letter] = 1

def create_hist(o_dict):
    for letter in sorted(o_dict.keys()):
        """ print times number of letters in the for loop """
        print(letter + "-"*(o_dict[letter]-1)+">")
        
        """print(o_dict[letter]) gives us their value which are integers"""
        # print(l + " = "+"*"*o_dict[letter])


print(o_dict)
create_hist(o_dict)

            
