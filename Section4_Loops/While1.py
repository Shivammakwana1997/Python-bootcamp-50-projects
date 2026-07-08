'''
Atm simulator

'''



def atm_simulator(balance:int,widthdrawal:int)->str:

    index = 0
    messages = []
    while index < len(widthdrawal):
        current_ammount = widthdrawal[index]

        if balance >= current_ammount:
            balance = balance - current_ammount
            messages.append(f"widthdraw successfull and amount is {current_ammount}")
        else:
            messages.append(f"insuffisent amount and amount is {current_ammount}")


        index += 1 


        messages.append(f"Remaining amount of current balance is {balance}")
        return messages  

    
balance = int(input("Enter the current balance : "))
widthdrawal = [int(input("Enter the widthdrawal amount : "))]
print(atm_simulator(balance,widthdrawal))           