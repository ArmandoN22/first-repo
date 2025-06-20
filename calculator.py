options = ["+", "-", "*", "/"]

while True:

    print("---- Menu ----")
    print("  sum (+)")
    print("  subtraction (-)")
    print("  multiplication (*)")
    print("  division (/)")

    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
    except ValueError:
        print("You must enter valid numbers.")
        continue



    option = input("\nChoose the operation you want to perform (+, -, *, /): ")

    if option not in options:
        print("\nInvalid option. Try again")
        continue

    if option == options[0]:
        result = number1 + number2
        print(f'The sum between {number1} {option} {number2} is: {result}')
    elif option == options[1]:
        result = number1 - number2
        print(f'The subtraction between {number1} {option} {number2} is: {result}')
    elif option == options[2]:
        result = number1 * number2
        print(f'The multiplication between {number1} {option} {number2} is: {result}')
    else:
        try:
            result = number1 / number2
            print(f'The division between {number1} {option} {number2} is: {result}')
        except ZeroDivisionError:
            print("Cann´t divide by 0")
 

    op2 = input("\nDo you want continue? y/n: ").lower().strip()
    if op2 == "n":
        break

