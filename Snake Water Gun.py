# Snake-Water-Gun Game
import random

lst = ['S', 'W', 'G']

chance = 10
num_of_chance = 0
computer_point = 0
human_point = 0

print("\t \t \t Snake-Water-Gun Game")
print("Press S for Snake, W for Water, G for Gun")

# developing the game using while
while num_of_chance < chance:
    inp = input("Snake-Water-Gun: ")
    _random = random.choice(lst)

    if inp == _random:
        print("Tie 0 Points to both \n")

    # if human enters S
    if inp == "S" and _random == "G":
        computer_point = computer_point + 1
        print(f"your guess is {inp} and computer guess is {_random}")
        print("Computer wins 1 point")
        print(f"Human points is {human_point} and Computer points is {computer_point}")

    elif inp == "S" and _random == "W":
        human_point = human_point + 1
        print(f"Your guess is {inp} and Computer Guess is {_random}")
        print("Human wins 1 point")
        print(f"Human points is {human_point} and Computer points is {computer_point}")

    # if human enters W
    elif inp == "W" and _random == "S":
        computer_point = computer_point + 1
        print(f"your guess is {inp} and computer guess is {_random}")
        print("Computer wins 1 point")
        print(f"Human points is {human_point} and Computer points is {computer_point}")

    elif inp == "W" and _random == "G":
        human_point = human_point + 1
        print(f"Your guess is {inp} and Computer Guess is {_random}")
        print("Human wins 1 point")
        print(f"Human points is {human_point} and Computer points is {computer_point}")

    # if human enters G
    elif inp == "G" and _random == "W":
        computer_point = computer_point + 1
        print(f"your guess is {inp} and computer guess is {_random}")
        print("Computer wins 1 point")
        print(f"Human points is {human_point} and Computer points is {computer_point}")

    elif inp == "G" and _random == "S":
        human_point = human_point + 1
        print(f"Your guess is {inp} and Computer Guess is {_random}")
        print("Human wins 1 point")
        print(f"Human points is {human_point} and Computer points is {computer_point}")

    num_of_chance = num_of_chance + 1
    print(f"{chance - num_of_chance} is left from {chance}")

print("Game Over")

if computer_point > human_point:
    print("Computer wins and human lost")
if human_point > computer_point:
    print("Human wins and Computer lost")

print(f"Human points are {human_point} and Computer points are {computer_point}")
