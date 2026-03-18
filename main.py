import random 

number = (random.randint(1,100))
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")

input_level = input("\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n\nEnter your choice:")

chances = 0
easy = chances + 10
medium = chances + 5
hard =  chances + 3

if input_level == "1":
    chances = 10
    difficulty = easy
elif input_level == "2":
    chances = 5
    difficulty = medium
elif input_level == "3":
    chances = 3
    difficulty = hard
else:
    print("\nLetra no reconocida\nIntenta de nuevo")

if input_level == "1":
    difficulty = easy
elif input_level == "2":
    difficulty = medium
elif input_level == "3":
    difficulty = hard
print(f"\nDifficulty : {difficulty}\nIntentos: {chances}\n")

while chances > 0:
    guess = int(input("Elige un numero del 1 al 100:"))
    chances -=1

    if guess == number:
        print("Felicidades, Acertaste!!!")
        break
    elif guess > number:
        print(f"\nEl numero es menor, Te quedan {chances} intentos!\n")
    else:
        print(f"\nEl numero es mayor. Te quedan {chances} intentos!\n")

if chances == 0 and guess != number:
    print(f"\nPerdiste, el numero era {number}")



