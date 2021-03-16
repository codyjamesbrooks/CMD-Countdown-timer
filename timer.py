import winsound
import time


class Countdown():
    """ Simple countdown timer. Asks user to enter the lenght of the timer in minutes.
    Then prints a formated sentence onto the Command line with the remaining number of 
    minutes and seconds. 
    When the countdown is finished program will beep, 12 times or until it is keyboard intrupted. 
    """

    def __init__(self):
        self.frequency = 750  # Set Frequency of alarm beep
        self.duration = 700  # Set Milliseconds of beep length
        # Intantiate the lenght of the timer in seconds.
        self.total_seconds = self.get_duration() * 60

    def countdown(self):
        # Function that does most of the work. takes the user inputed duration, and counts it down to zero.
        # Prints mins and seconds remaining on the timer.
        # Once it counts to zero it raises an audible alarm.
        while self.total_seconds >= 0:
            min_remain, sec_reamin = divmod(self.total_seconds, 60)
            print(
                'Time Remaining: {:02d} mins, {:02d} secs'.format(min_remain, sec_reamin), end='\r')
            self.total_seconds -= 1
            time.sleep(1)
        print('Time Remaining: {:02d} mins, {:02d} secs'.format(
            min_remain, sec_reamin))
        print("Thats time. Hit 'Ctrl-C' to end alarm")
        self.alarm()

    def alarm(self):
        # Sounds alarm. Alarm will sound 12 times. Stop alarm with 'ctrl' + 'C'
        counter = 0
        try:
            while counter < 12:
                winsound.Beep(self.frequency, self.duration)
                counter += 1
                time.sleep(3)
        except KeyboardInterrupt:
            pass

    def get_duration(self):
        # Get length of timer from user. Has a small amount of validation to check if the entered value is a number.
        print('How long should would you like to work for?')
        while True:
            time_mins = input("Minutes: ")
            try:
                time_mins = int(time_mins)
            except ValueError:
                print('Ya gotta enter a number')
                continue
            else:
                return time_mins


# Create the class. Start the countdown.
if __name__ == '__main__':
    mytimer = Countdown()
    mytimer.countdown()
