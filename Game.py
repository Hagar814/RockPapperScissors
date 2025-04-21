print("Let's play Rock Paper Scissors!")

loose = "The computer wins"
win = "Congratulations. YOU WIN"
playerScore = 0
pcScore = 0
newGame = 'y'

rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# === LOGIN SECTION ===
print("To begin, fill in the below information.")
username = input("Please enter username: ")
password = input("Please enter password: ")

found = False
with open("accounts.csv", "r") as searchfile:
    for line in searchfile:
        if username in line and password in line:
            found = True
            break

if found:
    print("Access Granted ✅\n")
    print("Available Moves:")
    print(rock_art)
    print(paper_art)
    print(scissors_art)

    import random

    while newGame.lower() == 'y':
        print(f"\nPlayer Score: {playerScore} | Computer Score: {pcScore}")
        player = input("Choose: Rock (r), Paper (p), Scissors (s): ").lower()
        move = ('r', 'p', 's')
        computer = random.choice(move)

        if player == 'r':
            if computer == 'p':
                print(rock_art + "                     " + paper_art)
                print(loose)
                pcScore += 1
            elif computer == 's':
                print(rock_art + "                     " + scissors_art)
                print(win)
                playerScore += 1
            else:
                print("DRAW")

        elif player == 'p':
            if computer == 'r':
                print(paper_art + "                     " + rock_art)
                print(win)
                playerScore += 1
            elif computer == 's':
                print(paper_art + "                     " + scissors_art)
                print(loose)
                pcScore += 1
            else:
                print("DRAW")

        elif player == 's':
            if computer == 'p':
                print(scissors_art + "                     " + paper_art)
                print(win)
                playerScore += 1
            elif computer == 'r':
                print(scissors_art + "                     " + rock_art)
                print(loose)
                pcScore += 1
            else:
                print("DRAW")

        else:
            print("Invalid input! Please choose r, p, or s.")

        newGame = input("Continue playing? (y/n): ")

    # === Final Score Summary ===
    print(f"\nFinal Score -> Player: {playerScore} | Computer: {pcScore}")
    if playerScore > pcScore:
        print(win)
    elif playerScore < pcScore:
        print(loose)
    else:
        print("DRAW")
    print("Thanks for playing 🎮")

else:
    print("Username or Password is incorrect ❌")
