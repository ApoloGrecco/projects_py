import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

selections = [rock, paper, scissors]

player_selection = int(input("what do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_selection = int(random.randint(0, 2))

print(f"{selections[player_selection]}")
print(f"Computer chose:\n {selections[computer_selection]}")


if (player_selection == 2 and computer_selection == 1) or (player_selection == 1 and computer_selection == 0) or (player_selection == 0 and computer_selection == 2):
    print("You win")
else:
    print("You lose")


