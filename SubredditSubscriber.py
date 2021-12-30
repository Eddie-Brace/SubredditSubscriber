from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary

#gobbles up text file of r/subredditname seperating by whitespace
#loads from that sub page and clicks join button
#do you REALLY need something better than O(n)??

driver = webdriver.Chrome()
print("First, login to Reddit in the Chrome window that just popped up.")
filename = input("Next, enter path of text file: ")
try:
    file = open(filename, "r")
except FileNotFoundError:
    print("File " + filename + " does not exist.")
    exit(1)

while True:
    line = file.readline().strip()
    if line == "": #end condition
        break

    driver.get("https://www.reddit.com/" + str(line))
    if driver.page_source.count("Joined") + driver.page_source.count("joined") > 2:
        print("Already subscribed to /" + line)
        continue

    try:
        button = driver.find_element_by_xpath("//button[text()='Join']").click()
        print('/' + line)
    except NoSuchElementException:
        print("/" + line + " might not exist.")

file.close()