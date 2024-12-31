import time
import winsound

def setAlarm():
    while True:
        try:
            askHour = int(input("Enter Hour You wanna set (0 - 23): "))
            askMin = int(input("Enter Min you wanna set (0 - 59): "))
            if 0 <= askHour <= 23 and 0 <= askMin <= 59:
                print("Alarm is set at ", askHour, ":", askMin)
                return askHour, askMin
            else:
                print("Invalid Input!")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def Alarm(hour, askHour, askMin, min):
    freq = 1000  # Hz
    dur = 500  # ms

    while True:
        hour = int(time.strftime("%H"))
        min = int(time.strftime("%M"))
        if hour == askHour and min == askMin:
            print("Current time: ", hour, ":", min)
            endTime = time.time() + 5
            while time.time() < endTime:
                winsound.Beep(freq, dur)
            break
                

def main():
    hour = int(time.strftime("%H"))
    min = int(time.strftime("%M"))
    askHour, askMin = setAlarm()  
    Alarm(hour, askHour, askMin, min)

main()