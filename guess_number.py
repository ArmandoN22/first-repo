import random
minimum = 1
attempts = 0


while True:

    while True:
        option = input("\nChoose difficulty: Easy(E) - Medium(M) - Hard(H): ").upper()

        if option not in ("E", "M", "H"):
            print("\nInvalid Option. Try again\n")
            continue

        if option == "E":
            maximum = 10
        elif option == "M":
            maximum = 50
        else:
            maximum = 100
        break

    random_number = random.randint(minimum,maximum)
    attempts = 0

    while True:

        while True:
            try:
                player_number = int(input(f'\nGuess the number between {minimum} and {maximum}: '))
                break
            except ValueError:
                print("You must enter a valid number.")

        attempts += 1

        if player_number < random_number:
            print("Very Low")
        elif player_number > random_number:
            print("Very High")
        else: 
            print("Correct!")
            break

    print(f'\nYou guessed the number in {attempts} attempts.')


    cont = input("\nDo you want continue play? Y/N: ").upper()

    if cont == "N":
        print("\nThanks for playing.")
        break

