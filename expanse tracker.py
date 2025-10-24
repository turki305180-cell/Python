print("(Expanse Tracker)")
store = dict()
while True:
        item = input("Enter an item: ").strip().lower().capitalize()
        if item.lower() == "quit":
            break
        value = input(f"Enter a Value for'{item}': ")
        try:
            store[item] = float(value)
        except:
             print("Error!: please write a number value not a letter")
dis = input("type Average to get the Average of the Values or type sum to sum your values: ").lower().strip()
if dis == "sum":
    sam = sum(store.values())
    print("the sum of the values: ",sam)
elif dis == "average":
    average = sum(store.values()) / len(store)
    print("the average of your items: ",average)
    
