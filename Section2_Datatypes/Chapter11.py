''' advanced datatypes 
datetime , time , calander
'''

# pyrefly: ignore [missing-import]
import arrow 

brewing_time = arrow .utcnow()
brewing_time = brewing_time.to("Europe/Berlin")
print(f"time in germany {brewing_time}")


from collections import namedtuple
chaiProfile = namedtuple("chaiProfile","masalachai kadakchai adrak chai")

print(chaiProfile)


