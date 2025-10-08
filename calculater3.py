while True:
    ope = input("enter a Mathematical operator: ")
    Numb = input("Enter a Number: ")
    numb = input("Enter another number: ")
    try:
        Num = float(Numb)
        num = float(numb)
    except:
        print("ERORR: please correct your input")
        continue
    if ope in ["x",'X','*']:
        sol = Num * num
        print(sol)
    elif ope in ["plus","Plus","+","PLUS"]:
        sol = Num + num
        print(sol)
    elif ope in ["subtraction","Subtraction","SUBTRACTION","-"]:
        sol = Num - num
        print(sol)
    elif ope in ["diviton","divide","/"]:
        sol = Num / num
        print(sol)
    elif ope not in ["plus","Plus","+","PLUS","subtraction","Subtraction","SUBTRACTION","-","diviton","divide","/","x",'X','*']:
        print("ERORR: please correct your input")
