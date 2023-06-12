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
#ASCI compile for show up in list[]
image=[rock,paper,scissors]
user_choice = int(input("Please entered: 0 for Rock, 1 for Paper and 2 for Scissors:\n"))
#here using if due to user having chosen between 1to2 and beyond this if input give invalid no.
if user_choice < 0 or user_choice>= 3:
    print("Invalid no. Game Selection")
else:
    print(F"User chosen {user_choice}")
    #image into list list indices use[]
    print(image [user_choice])
    # Indentation 
    import random
    computer_choice=random.randint(0,2)
    print(F"computer chosen {computer_choice}")
    print(image [computer_choice])

    #Game rule apply with if condition

    if user_choice<0 or computer_choice>=3:
        print("Invalid no. Game Selection")
    elif user_choice==0 and computer_choice==1:
        print("Rock beat the paper")
    elif user_choice==1 and computer_choice==2:
        print("Paper beat the scissors")
    elif user_choice==2 and computer_choice==0:
        print("Scissor beat the Rock")
    elif user_choice>computer_choice:
        print("You Won")
    elif user_choice==computer_choice:
        print("Withdraw")




