while True:
    try:
         operator = input("Enter a mathematical operator: ").lower().strip()
         num1 = float(input("Enter a Number: ").strip())
         num2 = float(input("Enter another Number: ").strip())
    except ValueError:
        print("Error!: please correct your input")
        continue
    if operator in ["x","*","multiplication"]:
        sol = num1 * num2
        print(sol)
    elif operator in ["addition","plus","+"]:
        sol = num1 + num2
        print(sol)
    elif operator in ["/","division","divide"]:
        if 0 == num2:
            print("Error!: can't divide by 0")
        else:
            sol = num1 / num2
            print(sol)    
    elif operator in ["-","subtraction","minus"]:
         sol = num1 - num2
         print(sol)
    else:
        print("Error!: Enter a vaild operator")
