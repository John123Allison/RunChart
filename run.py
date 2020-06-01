import math
import datetime

class Run:
    def __init__(self, date_raw, distance, time, pace, elevation):
        self.date = date_raw
        # convert raw string to datetime object
        self.distance = distance
        self.time = time
        self.pace = pace
        self.elevation = elevation
    def seconds_to_mins(self, time):
        return str(math.floor(time / 60)) + " mins " + str((time % 60)) + " seconds"
    def to_string(self):
        formatted_time = self.seconds_to_mins(self.time)
        formatted_pace = self.seconds_to_mins(self.pace)
        string = "Date: " + self.date + "\nDistance: " + str(self.distance) + " mile\nTime: " + formatted_time + "\nPace: " + formatted_pace + "\nElevation: " + str(self.elevation)
        return string