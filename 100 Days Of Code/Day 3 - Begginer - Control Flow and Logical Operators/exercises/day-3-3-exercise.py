# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print("Leep year. 3")
# print("Not leap year. 3")

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("Leap year.")
        else:
            print("Not Leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
