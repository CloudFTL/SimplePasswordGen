#importing shit
import random, string
#PEE PEE POO POO
#raw_input asking for user input to return as a string, then convert into an integer
password_length = int(input("HOW LONG DO U LIKE THEM?"))
#POO POO PEE PEE
password_characters = string.digits + string.punctuation
#sets a blank list (of strings, individual characters, but strings)
password = []
#LMAO PEEPEE
for x in range(password_length):    
    #hacker coder stuff lol
    password.append(random.choice(password_characters))
#doing stuff lmao
print(''.join(password))
