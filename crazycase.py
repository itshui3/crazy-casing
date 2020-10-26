import random
import string

string = input('Input a string to case: ')

crazy_cased = ''

for i in range(0, len(string)):

    if(random.choice([True, False])):
        crazy_cased += string[i].upper()
    else:
        crazy_cased += string[i].lower()

print(crazy_cased)