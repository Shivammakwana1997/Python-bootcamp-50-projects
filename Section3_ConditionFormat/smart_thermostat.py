def check_temperature(device_status:str , temperature:int) ->str:
    if device_status == "active":
        if temperature >= 35:
            return "Turn on AC"
        elif temperature <= 15:
            return "Turn on the Heater"
        else:
            return "Temperature is ideal"


    else: return "Device is inactive"

device_status = input("Enter the device status : ").lower()

if device_status in ["deactive", "inactive"]:
    print("Device is inactive")
else:
    temperature = int(input("Enter the temperature : "))
    print(check_temperature(device_status, temperature))
 