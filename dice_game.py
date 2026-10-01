import random


total_score = 0
player_name = str(input("Enter Your Name: "))
print(f"Welcome to THE DICE GAME {player_name}")
print("Your score should be above 20 to win the game")
print("Your score determines your reward")
print("Goodluck!")
failed_attempts = 0


for throw in range(0,6):
    decision = input("Push Enter ↵ to throw the dice or \"Q\" to quit: ")
    p_score = random.randint(0,5)
    if p_score == 0:
        failed_attempts += 1
    if decision == "Q":
        print("You quit the game")
        print(f"Number of throws: {throw}")
        print("The game is still yours!")
        print(f"Failed attempt is {failed_attempts}")
        break
    print(f"You score {p_score} point")
    total_score = total_score + p_score


print("Game Over")
print(f"Your Total score is {total_score}")

if total_score >= 20:
    print(f"Congratulations {player_name}, you won a trip around the world")
elif 15 < total_score < 20:
    print("Good game, you won a free class with your mentor")
else:
    print("Try Again!")
