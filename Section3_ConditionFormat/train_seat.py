seat_type = input("Enter seat type (sleeper/ac/non-ac/luxary):").lower()

match seat_type:
    case "sleeper":
        print("Price is : 500")
    case "ac":
        print("Price is : 800")
    case "non-ac":
        print("Price is : 300")
    case "luxary":
        print("Price is : 1200")

    