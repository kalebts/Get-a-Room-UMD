import csv
import os

# this is just a simple script to convert csv files containing
# the class day/time data into strings in JavaScript. I added 
# the resulting variables into the map code. This made it easier to
# demo the map on my phone.

# open folder
files = os.scandir("/Users/kalebtsegaye/Desktop/pyth/umd_schedule_scraper")

# start writing to text file
txt = open("vars.txt", "w")

# for each file in folder
for f in files:
    if (f.name[-3:] == "csv"): # if .csv file...
        with open((f.name), 'r') as csv_file: # read file
            s = "var " + f.name[0:3] + " = \"" # writing a new variable
            reader = csv.reader(csv_file)
            for row in reader: # writing data into variable, each row separated by \n
                s += row[0] + "," +  row[1] + "," + row[2] + "," + row[3] + "\\n"
            txt.write(s[0:(len(s)-2)] + "\"" + "\n")

txt.close()

print("done")
                
