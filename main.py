import random 

number = (random.randint(1,100))
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")

input_level = input("\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n\nEnter your choice:")

Chances = 0
Easy = Chances + 10
Medium = Chances + 5
Hard =  Chances + 3

if input_level == "1":
    Chances = 10
elif input_level == "2":
    Chances = 5
elif input_level == "3":
    Chances = 3
else:
    print("\nLetra no reconocida\nIntenta de nuevo")

if input_level == "1":
    Difficulty = Easy
elif input_level == "2":
    Difficulty = Medium
elif input_level == "3":
    Difficulty = Hard
print(f"\nDifficulty : {Difficulty}\nIntentos: {Chances}\n")

while Chances > 0:
    guess = int(input("Elige un numero del 1 al 100:"))
    Chances -=1

    if guess == number:
        print("Felicidades, Acertaste!!!")
        break
    elif guess > number:
        print(f"\nEl numero es menor, Te quedan {Chances} intentos!\n")
    else:
        print(f"\nEl numero es mayor. Te quedan {Chances} intentos!\n")

if Chances == 0 and guess != number:
    print(f"\nPerdiste, el numero era {number}")

