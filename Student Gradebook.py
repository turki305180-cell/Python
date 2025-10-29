print("(Student Gradebook)")
book = dict()
while True: 
    names = input("(type quit if your done) Enter Student name: ").strip().lower().capitalize()
    if names == "Quit":
        break
    try:  
       grade = float(input(f"Enter'{names}'Grade: ").strip())
       book[names] = grade
    except:
        print("Error!: The grade must not contain a letter please correct your input.")
action = input("to get the Average of the student grade type(Average), to get a sorted preformance list type(sort), to get both type(both):  ").strip().lower().capitalize()
 #this code sums the average    
if action == "Average":
    average = sum(book.values()) / len(book) 
    print("the Average of the students grade: ",average)
#this code sorts the dict()
elif action == "Sort":
    sart = dict(sorted(book.items(), key=lambda item: item[1], reverse=True))
    for k,v in sart.items():
        print(k,v)
#this code sums the average and give a sorted dictionary
elif action == "Both":
    average = sum(book.values()) / len(book)
    sart = dict(sorted(book.items(), key=lambda item: item[1], reverse=True))
    print("the Average of the students Grades: ", average)
    for k,v in sart.items():
       print(k,v)
    