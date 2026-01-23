choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter a number between 1 to 3 for the following choices: 1-Rock, 2-Paper, 3-Scissors: ")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice should be between 1 and 3!cls")