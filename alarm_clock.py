class AlarmClock:
    def __init__(self, time_passed_in, wake_up, alarm):
        self.current_time = time_passed_in
        self.alarm_time = wake_up
        self.alarm = alarm

    def set_current_time(self, updated_current_time):
        self.current_time == updated_current_time

    def set_alarm(self, alarm):
        self.alarm = alarm

    def set_alarm_time(self, wake_up):
        self.alarm_time = wake_up
