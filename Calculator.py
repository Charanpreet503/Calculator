print("|------      /\      |        |------  |      |  |            /\      ---------  |------|  |-----|  ")
print("|           /  \     |        |        |      |  |           /  \         |      |      |  |_____|  ")
print("|          /____\    |        |        |      |  |          /____\        |      |      |  |\       ")
print("|         /      \   |        |        |      |  |         /      \       |      |      |  | \      ")
print("|______  /        \  |______  |______  |______|  |______  /        \      |      |______|  |  \     ")
print("BY CHARANPREET")
while True:
    print("OPTIONS:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'age' to find your birth year")
    user_input = input(":")
    if user_input == "quit":
        break
    elif user_input == "add":
        #we used float because while doing any operation in decimal from , we will get accurate answer.
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1+num2)
        print("The answer is " + result)

    elif user_input == "subtract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
        print("The answer is " + result)

    elif user_input == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
        print("The answer is " + result)

    elif user_input == "divide":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
        print("The answer is " + result)

    elif user_input == "age":
        x = float(input("Enter the current year: "))
        y = float(input("Enter your age: "))
        print("This is your birth year")
        print(x - y)
    else:
        print("Unknown Input")