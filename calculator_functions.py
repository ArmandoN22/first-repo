def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

operations = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir
}

while True:
    print("\n---- Calculator Menu ----")
    print("  sum (+)")
    print("  subtraction (-)")
    print("  multiplication (*)")
    print("  division (/)")

    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ You must enter valid numbers.")
        continue

    operator = input("Choose the operation you want to perform (+, -, *, /): ").strip()

    if operator not in operations:
        print("❌ Invalid operation. Try again.")
        continue

    result = operations[operator](number1, number2)

    if isinstance(result, str):  # Error de división por 0
        print(result)
    else:
        print(f"✅ Result: {number1} {operator} {number2} = {result}")

    cont = input("Do you want to continue? (y/n): ").lower().strip()
    if cont == "n":
        break
