import math
import datetime

class Run:
    def __init__(self, date_raw, distance, time, pace, elevation):
        # convert raw string to datetime object
        date_raw = date_raw.replace('-', '')
        date_raw_year = int(date_raw[0:4])
        date_raw_month = int(date_raw[4:6])
        date_raw_day = int(date_raw[6:8])
        self.date = datetime.date(date_raw_year, date_raw_month, date_raw_day)

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