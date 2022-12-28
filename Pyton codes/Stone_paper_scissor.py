import random
#image of a rock to display
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#image of a paper to display
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
#image of a scisssor to display
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#list of all the images woth 0,1,2 index
game_images = [rock, paper, scissors]
#user choice taken from the user 
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#condition to check if the user choice is valid or not 
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!")
#if condition is valid then following condition will execute 
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
#programmed by Kirti Somnath Lulle
