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
    elif ope in ["diviston","divide","/"] and 0 not in [num]:
        sol = Num / num
        print(sol)
        print("ERROR: can divide 0")
    elif ope not in ["plus","+","subtraction","-","diviton","divide","/","x",'*']:
        print("ERROR: please correct your input")
    else:
        print("ERORR: can't divide 0 by",Num) 
