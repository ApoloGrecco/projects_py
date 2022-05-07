# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name_one_lower = name1.lower()
name_two_lower = name2.lower()
score_true = 0
score_love = 0

if name_one_lower.count("t") or name_two_lower.count("t"):
    score_true += name_one_lower.count("t")
    score_true += name_two_lower.count("t")
if name_one_lower.count("r") or name_two_lower.count("r"):
    score_true += name_one_lower.count("r")
    score_true += name_two_lower.count("r")
if name_one_lower.count("u") or name_two_lower.count("u"):
    score_true += name_one_lower.count("u")
    score_true += name_two_lower.count("u")
if name_one_lower.count("e") or name_two_lower.count("e"):
    score_true += name_one_lower.count("e")
    score_true += name_two_lower.count("e")

if name_one_lower.count("l") or name_two_lower.count("l"):
    score_love += name_one_lower.count("l")
    score_love += name_two_lower.count("l")
if name_one_lower.count("o") or name_two_lower.count("o"):
    score_love += name_one_lower.count("o")
    score_love += name_two_lower.count("o")
if name_one_lower.count("o") or name_two_lower.count("v"):
    score_love += name_one_lower.count("v")
    score_love += name_two_lower.count("v")
if name_one_lower.count("e") or name_two_lower.count("e"):
    score_love += name_one_lower.count("e")
    score_love += name_two_lower.count("e")

score_total = (score_true*10) + score_love

if 40 <= score_total <= 50:
    print(f"Your score is {score_total}, you are alright together")
elif score_total <= 10 or score_total >= 90:
    print(f"Your score is {score_total}, you go together like coke and mentos.")
else:
    print(f"Your score is {score_total}")


