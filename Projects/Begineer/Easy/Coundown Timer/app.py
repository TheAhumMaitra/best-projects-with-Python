import time

user_time = int(input("Enter time in seconds : "))
for i in reversed(range(0, user_time)):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600) % 24
    print(f"{hours : 0} : {minutes : 02} : {seconds : 02}")
    time.sleep(1)
print("Times up!")
