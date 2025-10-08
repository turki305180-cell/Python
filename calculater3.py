while True:
    ope = input("enter a Mathematical operator: ").lower()
    Numb = input("Enter a Number: ")
    numb = input("Enter another number: ")
    try:
        Num = float(Numb)
        num = float(numb)
    except:
        print("ERROR: please correct your input")
        continue
    if ope in ["x",'*']:
        sol = Num * num
        print(sol)
    elif ope in ["plus","+",]:
        sol = Num + num
        print(sol)
    elif ope in ["subtraction","-"]:
        sol = Num - num
        print(sol)
    elif ope in ["division","divide","/"] and num !=0:
        sol = Num / num
        print(sol)
    elif ope not in ["plus","+","subtraction","-","division","divide","/","x",'*']:
        print("ERROR: please correct your input")
    else:
        print("ERROR: can't divide by 0",Num)
        
