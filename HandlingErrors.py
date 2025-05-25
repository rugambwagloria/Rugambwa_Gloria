while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Please enter valid numbers.")
        continue
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero second number.")
        continue
    else:
        print("The result of " + str(num1) + " divided by " + str(num2) + " is " + str(result))
        break
    
    