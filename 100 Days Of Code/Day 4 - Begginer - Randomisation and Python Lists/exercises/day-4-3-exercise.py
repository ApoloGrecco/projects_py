# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

first_position = position[1]
second_position = position[0]

if first_position == "1":
    if second_position == "1":
        row1[0] = "X"
    elif second_position == "2":
        row1[1] = "X"
    else:
        row1[2] = "X"
elif first_position == "2":
    if second_position == "1":
        row2[0] = "X"
    elif second_position == "2":
        row2[1] = "X"
    else:
        row2[2] = "X"
else:
    if second_position == "1":
        row3[0] = "X"
    elif second_position == "2":
        row3[1] = "X"
    else:
        row3[2] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
