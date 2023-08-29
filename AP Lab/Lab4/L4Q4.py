from datetime import datetime

now = datetime.now()
time = now.strftime("%H:%M:%S")

name = input("Enter your name: ")

print("GREETINGS, ", name)
print("The time is: ", time)
