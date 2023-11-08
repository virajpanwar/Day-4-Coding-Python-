#rock paper scissor game
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
import random
print("Let's play rock paper scissors!\n")
print("What do you choose?\n")
user_choice = input("Type 0 for rock, 1 for paper, or 2 for scissors.")
if user_choice == "0":
  print(f"You chose rock!\n{rock}")
elif user_choice == "1":
  print(f"You chose paper!\n{paper}")
elif user_choice == "2":
  print(f"You chose scissors!\n{scissors}")
elif user_choice >= "3":
  print("Invalid input, you lose :(")
  quit()

uic=random.randint(0,2)
if uic == 0:
  print(f"The computer chose rock!\n{rock}")
elif uic == 1:
  print(f"The computer chose paper!\n{paper}")
elif uic == 2:
  print(f"The computer chose scissors!\n{scissors}")

if user_choice == "0" and uic == 0:
  print("It's a tie!")
elif user_choice == "0" and uic == 1:
  print("You lose!")
elif user_choice == "0" and uic == 2:
  print("You win!")
elif user_choice == "1" and uic == 0:
  print("You win!")
elif user_choice == "1" and uic == 1:
  print("It's a tie!")
elif user_choice == "1" and uic == 2:
  print("You lose!")
elif user_choice == "2" and uic == 0:
  print("You lose!")
elif user_choice == "2" and uic == 1:
  print("You win!")
elif user_choice == "2" and uic == 2:
  print("It's a tie!")
