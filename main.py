import check_input
import random

#Hailey Clark and Eric Andersen, 11/30/22, Group 15
#This program is a game where the user can bet money to try to guess the correct shell that is randomly assigned.


def main():
  #Setting initial values
  rep = True
  money = 100

  #While the user wants to continue playing and has enough money
  while (rep):

    #Printing the menu and getting the user's choice
    print("---------Shell Game---------")
    print("Find the ball to double your bet!")
    print()
    print("You have $", money)

    if (money < 20):
      print("Yikes! Hope you win this one...")
    if (money > 150):
      print("Wow! You sure you're not cheating?...")

    #User inputs the amount of money they want to bet
    bet = check_input.get_int_range("Bet amount? ", 1, money)

    #Creating the shells
    print("  ___     ___     ___")
    print(" /   \   /   \   /   \ ")
    print("/  1  \ /  2  \ /  3  \ ")
    print("------- ------- -------")

    #Gathering user's guess
    guess = check_input.get_int_range("Make a guess: ", 1, 3)

    #Randomly assigning the shell
    randVal = random.randint(1, 3)

    #Shells revealed
    print("  ___     ___     ___")
    print(" /   \   /   \   /   \ ")

    if (randVal == 1):
      print("/  $  \ /     \ /     \ ")
    elif (randVal == 2):
      print("/     \ /  $  \ /     \ ")
    elif (randVal == 3):
      print("/     \ /     \ /  $  \ ")

    print("------- ------- -------")

    #If the guess was incorrect, subtract the bet and tell user they lost
    if (randVal != guess):
      money -= bet
      print("Sorry... you lost $", bet, ". Your balance is currently $", money)
    #If the guess was correct, add the bet and tell user they won
    else:
      money += bet
      print("Congratulations! you earned $", bet, ". Your balance is now $",
            money)

    #If the user still has money, ask if they want to repeat
    if (money > 0):
      rep = check_input.get_yes_no("Play again? (y/n) ")

    #If money is 0 or less, tell user they are out of money and end the program
    else:
      print("You are out of money. Better luck next time!")
      rep = False


main()
