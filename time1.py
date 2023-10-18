class Time:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

    def setTime(self, hours, minutes, seconds, milliseconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.milliseconds = milliseconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}.{self.milliseconds:03d}"