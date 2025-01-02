import pyttsx3
import time
import winsound

def service():
    print("1. Tell me the current time")
    print("2. Set an alarm")
    print("3. Greet me with my name")
    print("4. Exit")

def settingEngine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.8)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    return engine

def firstService(engine):
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    engine.say(f"Current time is {hour} hours and {minute} minutes.")
    engine.runAndWait()

def secondService(engine):
    try:
        setHour = int(input('Set Hour (0 - 23): '))
        setMinute = int(input('Set Minute (0 - 59): '))

        print(f"Alarm set for {setHour:02}:{setMinute:02}")
        engine.say(f"Alarm set for {setHour:02}:{setMinute:02}")
        engine.runAndWait()

        while True:
            currentHour = int(time.strftime("%H"))
            currentMinute = int(time.strftime("%M"))
            if currentHour == setHour and currentMinute == setMinute:
                engine.say("Alarm ringing!")
                engine.runAndWait()
                for _ in range(10):
                    winsound.Beep(1000, 500)
                break
            time.sleep(10)  # This is used to reduce CPU usage by chceking every 10 second
    except ValueError:
        engine.say("Invalid input!")
        engine.runAndWait()

def thirdService(engine):
    user_name = input("What is your name? ")
    engine.say(f"Hello {user_name}, nice to meet you!")
    engine.runAndWait()

def main():
    engine = settingEngine()
    service()
    while True:
        try:
            choice = int(input("How may I help you? (1-4): "))
            if choice == 1:
                firstService(engine)
            elif choice == 2:
                secondService(engine)
            elif choice == 3:
                thirdService(engine)
            elif choice == 4:
                engine.say("Goodbye!")
                engine.runAndWait()
                break
            else:
                engine.say("Invalid input!")
                engine.runAndWait()
        except ValueError:
            engine.say("Invalid input!")
            engine.runAndWait()

if __name__ == "__main__":
    main()
