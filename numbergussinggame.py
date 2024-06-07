import random
n = random.randrange(0,10)
#print(n)
guess = int(input("Enter the number between 1 to 10:"))
while n != guess:
    if guess < n:
        print("your guess number is low!")
        guess = int(input("Enter the guess number again! :"))
    elif guess > n:
        print("your guess number is to high!")
        guess = int(input("Enter the guess number again! :"))
    else:
        break
print("your guess number is right!")
    
