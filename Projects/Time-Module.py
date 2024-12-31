import time as t

# hour = int(t.strftime("%H"))
# min = int(t.strftime("%M"))
# sec = int(t.strftime("%S"))

# time = ("Now time is ", hour, ": ", min, ": ", sec)

# if (int(hour) >= 5 and int(hour) < 12):
#     print("Good Morning!")
# elif (int(hour) >= 12 and hour < 17):
#     print("Good Afternoon!")
# elif (int(hour) >= 17 and hour < 24):
#     print("Good Night!")
# else:
#     print("Sooja Bhai!")









# time = ("Now time is ", hour, ": ", min, ": ", sec)

while True:
    hour = int(t.strftime("%H")) - 12
    min = int(t.strftime("%M"))
    sec = int(t.strftime("%S"))
    ms = int(t.strftime("%S")) * 1000


    time = (hour, ": ", min)
    print(ms)
    if ms == 1:
        print(time)