from datetime import datetime
from playsound import playsound
import winsound

alarm_date = input("Enter the date on which you want to set the alarm (DD-MM-YYYY): ").strip()
alarm_time = ''.join(input("Enter the time of alarm to be set in HH:MM AM/PM format: ").split())
Music_or_Beep = input("Enter M for music or B for beep: ").lower()

if Music_or_Beep == 'b':
    duration = int(input("Enter Duration (in seconds) "))*1000
    frequency = int(input("Enter frequency of beep (Optimal fre is 500Hz) "))

a_date = alarm_date[:2]    #DD
alarm_hour = alarm_time[:2]
alarm_minute = alarm_time[3:5]
alarm_period = alarm_time[5:8].upper()

print("Setting your alarm...\nHurray, alarm set-up successful")
print("Alarm will ring at", alarm_time + " on date", alarm_date)

while True:
    current_time = datetime.now()
    current_hour = current_time.strftime('%I')
    current_minute = current_time.strftime('%M')
    current_period = current_time.strftime('%p')
    current_date = current_time.strftime('%d')

    if current_date == a_date and current_period == alarm_period and current_hour == alarm_hour and current_minute == alarm_minute:
        print("Hello, wake up fast....\nAlarm ringing...!...!...!..!")
        if Music_or_Beep == 'm':
            playsound('audio.wav')
            print("Have a nice day..  Thanks for using Python's Alarm...")
            print("Do Subscribe, Like, Share and Comment!")

        else:
            winsound(frequency,duration)
            print("Have a nice day..  Thanks for using Python's Alarm...")
            print("Do Subscribe, Like, Share and Comment!")
        break