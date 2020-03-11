import json
import random

password_list = []
password = ""

with open("wordlist.json", "r") as w_file:
    wordlist = json.load(w_file)


while len(password_list) < 9:
    password_list.append(wordlist[random.randint(0, len(wordlist))])

for elem in password_list:
    if password == "":
        password = password + elem
    else:
        password = password + "-" + elem

print("Your new password is:", password, " -- write it in a secure place.")
