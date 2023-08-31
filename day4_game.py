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
rule=[rock,paper,scissors]
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user>=0 and user<=2:
    comp=random.randint(0,2)
    print(f"u chose:\n{rule[user]}")
    print(f"computer choose:{rule[comp]}")
    if user==0 and comp==1:
        print("u lost the game")
    elif user==1 and comp==2:
        print("u lost the game")
    elif user==2 and comp==0:
        print("u lost the game")
    elif user==comp:
        print("its a draw")
    else:
        print("u won the game")
else:
    print("sorry u entered an invalid entry")