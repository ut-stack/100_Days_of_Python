#15 Day15 - Exercise 2 - Good Morning Sir

import time 
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)



# Get the current hour as an integer
timestamp = int(time.strftime('%H'))
print(timestamp)

# Compare the current hour and print the appropriate greeting
if 21 <= timestamp or timestamp < 4:
    print("Good Night")
elif 4 <= timestamp < 12:
    print("Good Morning")
elif 12 <= timestamp < 16:
    print("Good Afternoon")
elif 16 <= timestamp < 21:
    print("Good Evening")
