import sys

if __name__ == "__main__":
    print("Don't do that!")
    # sys.exit()


s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])
 





the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)




# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

cipher = input('Enter your cryptogram: ')
text = ''
key = 1
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - key
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)


# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")





##line 03: ask the user to enter the IBAN (the number can contain spaces, as they significantly improve number readability...
##line 04: ...but remove them immediately)
##line 06: the entered IBAN must consist of digits and letters only – if it doesn't...
##line 07: ...output the message;
##line 08: the IBAN mustn't be shorter than 15 characters (this is the shortest variant, used in Norway)
##line 09: if it is shorter, the user is informed;
##line 10: moreover, the IBAN cannot be longer than 31 characters (this is the longest variant, used in Malta)
##line 11: if it is longer, make an announcement;
##line 12: start the actual processing;
##line 13: move the four initial characters to the number's end, and convert all letters to upper case (step 02 of the algorithm)
##line 14: this is the variable used to complete the number, created by replacing the letters with digits (according to the algorithm's step 03)
##line 15: iterate through the IBAN;
##line 16: if the character is a digit...
##line 17: just copy it;
##line 18: otherwise...
##line 19: ...convert it into two digits (note the way it's done here)
##line 20: the converted form of the IBAN is ready – make an integer out of it;
##line 21: is the remainder of the division of iban2 by 97 equal to 1?
##line 22: If yes, then success;
##line 23: Otherwise...
##line 24: ...the number is invalid.
##Let's add some test data (all these numbers are valid – you can invalidate them by changing any character).
##
##British: GB72 HBZU 7006 7212 1253 00
##French: FR76 30003 03620 00020216907 50
##German: DE02100100100152517108
##If you are an EU resident, you can use you own account number for tests.

    
