from alarm_clock import AlarmClock

clock_set_up = AlarmClock(input('Enter current time: '), input(
    'what time would you like to get up?: '), False)
print(f'you set the time to {clock_set_up.current_time}')
print(f'your alarm will be going off at {clock_set_up.alarm_time}')
print(f'is your alarm set? {clock_set_up.alarm}')
