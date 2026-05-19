import random

secret = random.randint(1,100)
attempts = 0
max_attempts = 7
print("Guess 1-100 (7 tries max)")
while attempts < max_attempts:
    guess = int(input("Guess:"))
    attempts += 1

    if guess == secret:
        print(f"Won in {attempts} tries!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    print(f"Tries left:{max_attempts-attempts}")
else:
    print(f"Lost! Secret: {secret}")