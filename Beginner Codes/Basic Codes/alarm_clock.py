import datetime
import time

def main():
    while True: # unless correct format of alarm
        alarm_time = input("At what time do you want the alarm to ring (HH:MM:SS)? ")
        if check_alarm_time(alarm_time) != False:
            break
        
    temp = check_alarm_time(alarm_time)
    countdown(temp[0], temp[1], temp[2])
     
    
def check_alarm_time(alarm): 
    if alarm.count(":") != 2: 
        return False
    
    hours, minutes, seconds = alarm.split(":")
    hours = int(hours.strip())
    minutes = int(minutes.strip())
    seconds = int(seconds.strip())
    
    # Check range of time
    if not (0 <= hours < 24 and 
            0 <= minutes < 60 and
            0 <= seconds < 60):
        return False
    else:
        return (hours, minutes, seconds)
    
    

def countdown(hours, minutes, seconds): 
    alarm_time = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
     
        if current_time == alarm_time:
            print("WAKE UP FROM YOUR SLEEEPPPPP!!! 💤😴🛌")
            break
        
        time.sleep(1)

if __name__ == "__main__":
    main()
    
    
''' in this alarmclock, I should've the ability to keep showing what the current time is right now
 (hrs, min, secs), and I should prompt the user for a time.
 
 if the countdown of the timer that I create becomes equal to the alarm time the user kept,
 I shall notify'''
 
''' *** My algorithm for this code ** '''
''' 
Step 1: ask the user at what time should alarm ring
Step 2: keeep printing the countdown of the present time
Step 3: if the alarm time that user sets = present time, stop code

'''