Hello!

This was a personal project completed in early 2019, to be displayed and shown at the American Association of Geographers Poster Symposium that same year. The purpose of this project was to create an interactive web map of the University of Maryland campus to display currently vacant rooms in every building. This was done by scraping class schedules from the school's website, grouping the data by building, mapping the data to each building, and writing code to figure out what rooms are not holding a class at the time they are being checked.

Just a quick overview of the files in this folder.

umd_schedule_scraper.py - the script used to retrieve class data from the UMD Schedule of Classes website
create_builing_csv_files.py - the script to organize the class data into .csv files for each building
csv_to_JS_vars.py - the script for converting the reorganized data into JavaScript variables. This was to help make an easier demo of the map.
final_map.html - the final map

I also included a .csv of a building as an example.

Kaleb Tsegaye