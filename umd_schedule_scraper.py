#importing the library
import requests
import urllib
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# setting up the script to scrape the websites
driver = webdriver.Firefox(executable_path='/Users/kalebtsegaye/Downloads/geckodriver')
driver.get("https://app.testudo.umd.edu/soc/201908")

main_page = driver.page_source # html code of schedule of classes website home page

driver.quit()

main_soup = BeautifulSoup(main_page, 'html.parser') # parse html

# retreiving all departments from home page
dept_box = main_soup.find_all('span', attrs = {'class' : "prefix-abbrev push_one two columns"})
dept = []

print(len(dept_box))

for i in range(len(dept_box)):
    dept.append(dept_box[0])

for i in range(len(dept_box)):
    dept[i] = dept_box[i].text.strip()

# for each department, open their website and get the class data
for i in range(len(dept)):
    # opening the site
    driver = webdriver.Firefox(executable_path='/Users/kalebtsegaye/Downloads/geckodriver')
    site = "https://app.testudo.umd.edu/soc/201908/"
    site = site + dept[i]
    print(site)

    driver.get(site)
    time.sleep(3)
    
    # clicking a button on website to display all of the course's information
    driver.find_element_by_id('show-all-sections-button').click()
    time.sleep(3)

    # driver2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "show-all-sections-button")))

    page = driver.page_source

    driver.quit()

    #beautful soup parses the html and puts it into soup
    soup = BeautifulSoup(page, 'html.parser')

    days = []
    start_time = []
    end_time = []
    building_code = []
    class_room = []

    # days.append(soup.find('span', attrs = {'class' : "section-days"}))
    # start_time.append(soup.find('span', attrs = {'class' : "class-start-time"}))
    # end_time.append(soup.find('span', attrs = {'class' : "class-end-time"}))
    # building_code.append(soup.find('span', attrs = {'class' : "building-code"}))
    # class_room.append(soup.find('span', attrs = {'class' : "class-room"}))

    section = soup.find_all('div', attrs = {'class' : "class-days-container"})

    for s in section: # for each class section
        dn = s.find('span', attrs = {'class' : "section-days"})
        stn = s.find('span', attrs = {'class' : "class-start-time"})
        etn = s.find('span', attrs = {'class' : "class-end-time"})
        bcn = s.find('span', attrs = {'class' : "building-code"})
        crn = s.find('span', attrs = {'class' : "class-room"})

        # putting all class location and time info into lists declared above
        if (dn == None):
            days.append("N/A")
        else:
            days.append(dn.text.strip())
        
        if (stn == None):
            start_time.append("N/A")
        else:
            start_time.append(stn.text.strip())

        if (etn == None):
            end_time.append("N/A")
        else:
            end_time.append(etn.text.strip())

        if (bcn == None):
            building_code.append("N/A")
        else:
            building_code.append(bcn.text.strip())

        if (crn == None):
            class_room.append("N/A")
        else:
            class_room.append(crn.text.strip())

            
    # writes it to a csv file, one csv file for each department
    
    with open((dept[i] + ".csv"), 'w') as csv_file:
            print("THIS IS THE DEPT: " + dept[i])
            writer = csv.writer(csv_file)
            for i in range(len(days)): 
                writer.writerow([days[i], start_time[i], end_time[i],
                                        building_code[i], class_room[i]])

    driver.quit()


print("done")
