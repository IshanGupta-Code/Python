import random

# 1 for Snake, -1 for Water, 0 for Gun
youDict = {"s": 1, "w": -1, "g": 0}
revDict = {1: "Snake", -1: "Water", 0: "Gun"}

computer = random.choice([0, -1, 1])

yourStr = input("Enter your Choice (s for Snake, w for Water, g for Gun): ").lower()
you = youDict.get(yourStr)

print(you)

if you not in [1, -1, 0]:
    print("Choose appropriate options")
else:
    print(f"You chose {revDict[you]} \nComputer chose {revDict[computer]}")

    if computer == you:
        print("It's a Draw")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You Win!!!")
    else:
        print("You Lose!!!")