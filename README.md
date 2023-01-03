# PythonProject
1.BMI_calculator.py:
  BMI is nothing but body mass index calculator:
  #start the program
  To calculate BMI we take two inputs Weight and height.
  Now we will calculate value using the given formula and store in the variable(BMI) BMI= (Weight of body/height**2).
  After we use conditional statements for the further calculation
  if BMI<18.5 then we will print you are underweight.
  else if (elif) BMI<25 then we will print you are normalweight.
  else if(elif) BMI<30 then we will print you are slightly overweight.
  else if(elif) BMI<35 then we will print you are obese.
  else we will print you are clinically obese.
  #end of program
  In this BMI_calculator.py we calculate Body Mass Index using the conditional statements.
 2.Stone_paper_scissor.py:
   stone paper scissor is a game that we will build using python 
   here we will use if else condition statements for implementation
   #start the program
   first we will import images of stone , paper and scissor and store them in variables
   now we will store these variables in the list game_images with indexing 0,1,2
   now we take input from the user either 0, 1 or 2 for rock, paper and scissor
   after that we will use if condition to check whether user have given 0, 1 or 2
   if user_choice>=3 or user_choice<0 then it will say invalid number
   else it will print user_choice and takes a random computer choice for computer choice we use random function
        that we import using #import random at the begining of the code also we use randint(0,2)to get inputs 0,1,2
        and will print the computer's random choice
        if user_choice == 0 and computer_choice == 2 then it will print you won!
        elif user_choice == 2 and computer_choice==0 then it will print you lost!
        elif computer_choice > user_choice then it will print you lost!
        elif user_choice > computer_choice then it will print you win!
        else it will print the match is draw!
  #end of program
  
  
  
