Staff = [("Amit",16) , ("zara",17), ("raj",28), ("simran",18)]


for (name,age) in Staff:
    if age > 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("no one is eligible")