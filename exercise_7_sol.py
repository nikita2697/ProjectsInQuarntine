from datetime import datetime
import time
from pygame import mixer
def play_music():
    mixer.init()
    mixer.music.load('water.mp3')
    mixer.music.play(-1)


    while (True):
        user_ip = input("Enter done to Stop Alarm!!\n")
        if user_ip == "done":
            mixer.music.stop()
            break

def log_file(msg):
    with open("MyLog1.txt", "a") as f:
        f.write(f"{msg}:\t[{datetime.now()}]\n")

if __name__ == '__main__':
    water_time=time.time()
    break_time = time.time()
    water_time_interval= 45
    break_time_interval=52
    lunch_time="16:55:00"

    while True:
        if time.time() - water_time > water_time_interval:
            print("Time To Drink Water.Take a sip!!!")
            water_time = time.time()
            play_music()
            log_file("Water Drink At:")

        if time.time() - break_time > break_time_interval:
            print("Time To Take a Small Break Relax!!!")
            break_time = time.time()
            play_music()
            log_file("Took break at:")

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if lunch_time==current_time:
            print("Time To Lunch!!!")
            break_time = time.time()
            play_music()
            log_file("Had a lunch at:")

