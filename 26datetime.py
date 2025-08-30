# import datetime
# now=datetime.datetime.now()
# hour=now.hour

# if hour<12:
#     print("Good Morning")
# elif hour<15:
#     print("Good Afternoon")
# else:
#     print("Good Evening")

import datetime
now=datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))