import random

perfect_num = random.randint(1, 1000)
print("Perfect Number (Hidden) = ", perfect_num)  # Hide this line during real play

guess = int(input("Enter Your Guessed Number: "))

while perfect_num != guess:
    if guess > perfect_num:
        print("Your number is greater than the Perfect Number")
    else:
        print("Your number is smaller than the Perfect Number")
    
    guess = int(input("Enter Your Guessed Number: "))

print("🎉 Congratulations! You guessed the Perfect Number!")

