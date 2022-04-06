import csv
import os

# i had to retreive data from umd's website by getting class data by department.
# i need to reorganize this data so the data is bundled together by their building.
# this is the purpose of this script.

print(os.getcwd())
# open files in directiory
files = os.scandir("/Users/kalebtsegaye/Desktop/pyth/umd_schedule_scraper/classes")

bc = []

# for each file
for f in files:
    if (f.name != "geckodriver.log"):
        with open(("classes/" + f.name), 'r') as csv_file: # read csv file
                reader = csv.reader(csv_file)
                for row in reader:
                    if (len(row[3]) == 3 and row[3] != 'N/A'):
                        # if 4th row is 3 characters, meaning it represents a building code,
                        # and is not "N/A", append the building code to bc array
                        bc.append(row[3])


# bc now has every building code referenced in the class data

# this code removes duplicate building codes
bc = list(dict.fromkeys(bc))

#this sorts the codes alphabetically
bc.sort()

print(bc)


# this commented out code created the csv files for each building code
# only ran this part once, which is why it is commented out

# for b in bc:
#     with open(b + '.csv', 'w') as csv_file:
#         writer = csv.writer(csv_file)

# open current directory (files) and directory of the class department csv files (cfiles)
files = os.scandir("/Users/kalebtsegaye/Desktop/pyth/umd_schedule_scraper")

cfiles = os.scandir("/Users/kalebtsegaye/Desktop/pyth/umd_schedule_scraper/classes")

# for each file in class department directory
for cf in cfiles:
    if (cf.name != "geckodriver.log"):
        with open(("classes/" + cf.name), 'r') as csv_file: # read csv file
            reader = csv.reader(csv_file)
            for row in reader:
                if (len(row[3]) == 3 and row[3] != 'N/A'): # if valid building code
                    with open((row[3] + ".csv"), 'a') as csv_file2: # append data to appropriate building csv
                        writer = csv.writer(csv_file2)
                        writer.writerow([row[0], row[1], row[2], row[4]])        




                
            