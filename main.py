import run
import sys
import json
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import numpy as np

# function to add to JSON 
# https://www.geeksforgeeks.org/append-to-json-file-using-python/
def write_json(data, filename='data.json'): 
    with open(filename,'w+') as f: 
        json.dump(data, f, indent=4) 

def analyze_runs(y_axis_data):
    try:
        with open('data.json') as file:
            data = json.load(file)
        runs = []

        for i in data.values():
            for j in i:
                obj = run.Run(j['date'], j['distance'], j['time'], j['pace'], j['elevation'])
                runs.append(obj)

        # make arrays of the axes
        dates_x = []
        for r in runs:
            date = r.date
            dates_x.append(date)
        data_y = []
        for r in runs:
            if y_axis_data == "pace":
                data_y.append(r.pace) 
            elif y_axis_data == "distance":
                data_y.append(r.distance)

        fig, ax = plt.subplots()
        ax.plot(dates_x, data_y) 

        # format the ticks
        # https://matplotlib.org/examples/api/date_demo.html
        myFmt = mdate.DateFormatter('%Y-%m-%d')
        ax.xaxis.set_major_formatter(myFmt)
        fig.autofmt_xdate()

        plt.show()

    except:
        print("No data.json exists yet. Try logging some runs!")

def log_run():
    # collect user input
    date = input("Run date? Format: yyyy-mm-sd: ")
    distance = float(input("Distance (miles): "))
    time_minutes = input("Time minutes: ")
    time_seconds = input("Time seconds: ")
    time = int(time_minutes) * 60 + int(time_seconds)
    pace = time / distance
    elevation = input("Elevation (ft): ")

    # make a dictionary from the input
    run = {
        "date":date,
        "distance":distance,
        "time":time,
        "pace":pace,
        "elevation":elevation
    }

    # append 
    with open('data.json') as json_file: 
        data = json.load(json_file) 
        
        temp = data["runs"] 
    
        # appending data to runs
        temp.append(run) 
      
    write_json(data)  

def help_me():
    print("Usage: python3 main.py [flags]")
    print("Flag 1: Use -l to log a run, or -s to display your data.")
    print("Flag 2: Use -p to display pace data, use -d to display distance data.")

def main(args):
    # check to see if data file exists, and create with template if not
    temp_dict = {"runs": []}
    if not os.path.exists('data.json'):
        write_json(temp_dict)

    # check to see if any args besides filename were passed
    if len(args) <= 1:
        print("Not enough args. Use -h for help.")
        quit()

    # operating mode
    mode = ""

    flags = args[1:]

    # check flags for options
    if flags[0] == "-h":
        mode = "help"
    elif flags[0] == "-l":
        mode = "log"
    elif flags[0] == "-s":
        mode = "show"
    else:
        print("Invalid options. Use -h for help.")

    if mode == "help":
        help_me()
    elif mode == "log":
        log_run()
    elif mode == "show":
        if len(flags) == 1:
            print("Needs more arguments! Use -h for help.")
        elif len(flags) > 1: 
            if flags[1] == "-p":
                analyze_runs("pace")
            elif flags[1] == "-d":
                analyze_runs("distance")
        else:
            print("Error")

if __name__ == "__main__":
    main(sys.argv)