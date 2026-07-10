users =[
    {"id":1,"total":100,"coupon":"P120"},
    {"id":2,"total":500,"coupon":"F50"},
    {"id":3,"total":400,"coupon":"F40"}]

discounts = {
    "P120" : (0.2,0),
    "F50"  : (0.2,0),
    "F40"  : (0,10),
}

for user in users:
    percent , fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"] * percent + fixed
    final = user["total"] - discount 
    print(user["id"] , final , user["coupon"] )