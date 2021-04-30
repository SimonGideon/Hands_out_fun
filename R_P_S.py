from random import randint
move = ["rock", "paper", "scissors"]
while True:
    computer = move[randint(0,2)]
    player = input("Enter: Rock, Scissors, Paper ? or stop!" )
    if player == 'stop!':
        print("Game ended..")

        break
    elif player == computer:
        print("A ties!")
    elif player == 'Rock':
        if computer == 'Paper':
            print("You lose", computer, "beat", player)
        else:
            print("You win", player, "beat", computer)
    elif player == 'Paper':
        if computer == 'Scissor':
            print("You lose", computer, "beats", player)
        else:
            print("You win", player, "beats", computer)
    elif player == 'Scissors':
        if computer == 'Rock':
            print("You lose", computer, "beats", player)
        else:
            print("You win", player, "beats", computer)
    elif player == computer:
        print("Tie")
    else:
        print("Check your spelling...")







