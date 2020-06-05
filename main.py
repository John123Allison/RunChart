import run
import sys
import json
import matplotlib.pyplot as plt
import numpy as np

# function to add to JSON 
# https://www.geeksforgeeks.org/append-to-json-file-using-python/
def write_json(data, filename='data.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

def analyze_runs(y_axis_data):
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
        dates_x.append(r.date)
    data_y = []
    for r in runs:
        if y_axis_data == "pace":
            data_y.append(r.pace) 
        elif y_axis_data == "distance":
            data_y.append(r.distance)

    plt.plot_date(dates_x, data_y) 
    plt.show()   

def log_run():
    date = input("Run date? Format: yyyy-mm-sd: ")
    distance = int(input("Distance (miles): "))
    
    time_minutes = input("Time minutes: ")
    time_seconds = input("Time seconds: ")
    time = int(time_minutes) * 60 + int(time_seconds)

    pace = time / distance

    elevation = input("Elevation (ft): ")

    run = {
        "date":date,
        "distance":distance,
        "time":time,
        "pace":pace,
        "elevation":elevation
    }

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
    # check to see if any args besides filename were passed
    if len(args) <= 1:
        print("Not enough args. Use -h for help.")
        quit()

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
    elif mode == "data":
        if flags[1] == "-p":
            analyze_runs("pace")
        elif flags[1] == "-d":
            analyze_runs("distance")
        else:
            print("Need another argument! Use the -h flag for help.")

if __name__ == "__main__":
    main(sys.argv)