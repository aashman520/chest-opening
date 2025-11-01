import random #Comment should be used

game = ["Rock🪨", "Paper📃", "Scissor✂️"]
print("1.Rock  2.Paper  3.Scissor")

inpt = input("Enter your choice (1, 2, 3): ")

if inpt in ["1", "2", "3"]:#Checks if input is entered properly.
    userchoice = game[int(inpt) - 1]
    Oppenentchoise = random.choice(game)

    print("You chose:", userchoice)
    print("Opponent chose:", Oppenentchoise)

    if userchoice == Oppenentchoise:
        print("It's a Tie!")
    elif (userchoice == "Rock🪨" and Oppenentchoise == "Scissor✂️") or \
         (userchoice == "Paper📃" and Oppenentchoise == "Rock🪨") or \
         (userchoice == "Scissor✂️" and Oppenentchoise == "Paper📃"):
        print("You Win!")
    else:
        print("You Lose!")
else:
    print("❌ Wrong Input! Please enter 1, 2, or 3.")
