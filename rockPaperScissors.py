import random as rd

pWins = 0
aiWins = 0

while True:
    pChoice = input(""" 
    Make your choice:
    Rock, Paper, or Scissors
    """).strip().lower()

    aiParameters = ["rock", "paper", "scissors"]
    aiChoices = rd.choice(aiParameters)

    if pChoice == "rock":
        if aiChoices == aiParameters[0]:
            print("You chose 'rock'; the AI chose 'rock'. 'Rock' and 'rock' TIES. AI and player TIES.")
            print(f"Player: {pWins}, AI: {aiWins}")
        elif aiChoices == aiParameters[1]:
            print("You chose 'rock'; the AI chose 'paper'. 'Paper' beats 'rock'. AI WINS.")
            aiWins += 1
            print(f"Player: {pWins}, AI: {aiWins}")
        elif aiChoices == aiParameters[2]:
            print("You chose 'rock'; the AI chose 'scissors'. 'Rock' beats 'scissors'. You WIN.")
            pWins += 1
            print(f"Player: {pWins}, AI: {aiWins}")

    elif pChoice == "paper":
        if aiChoices == aiParameters[0]:
            print("You chose 'paper'; the AI chose 'rock'. 'Paper' beats 'rock'. You WIN.")
            pWins += 1
            print(f"Player: {pWins}, AI: {aiWins}")
        elif aiChoices == aiParameters[1]:
            print("You chose 'paper'; the AI chose 'paper'. 'Paper' and 'paper' TIES. AI and player TIE.")
            print(f"Player: {pWins}, AI: {aiWins}")
        elif aiChoices == aiParameters[2]:
            print("You chose 'paper'; the AI chose 'scissors'. 'Scissors' beats 'paper'. AI WINS.")
            aiWins += 1
            print(f"Player: {pWins}, AI: {aiWins}")

    elif pChoice == "scissors":
        if aiChoices == aiParameters[0]:
            print("You chose 'scissors'; the AI chose 'rock'. 'Rock' beats 'scissors'. AI WINS.")
            aiWins += 1
            print(f"Player: {pWins}, AI: {aiWins}")
        elif aiChoices == aiParameters[1]:
            print("You chose 'scissors'; the AI chose 'paper'. 'Scissors' beats 'paper'. You WIN.")
            pWins += 1
            print(f"Player: {pWins}, AI: {aiWins}")
        elif aiChoices == aiParameters[2]:
            print("You chose 'scissors'; the AI chose 'scissors'. 'Scissors' and 'scissors' TIES. AI and player TIE.")
            print(f"Player: {pWins}, AI: {aiWins}")
    else:
        print("Invalid choice. Please choose 'Rock', 'Paper', or 'Scissors'.")

    if pWins == 3:
        print("The player wins the game. AI loses.")
        input("Waiting for next user input to close the game.")
        break
    elif aiWins == 3:
        print("The AI wins the game. The player loses.")
        input("Waiting for next user input to close the game.")
        break