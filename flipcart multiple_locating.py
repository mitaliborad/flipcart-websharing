#import statements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Opens Flipkart's search results for the query "mobile."
driver = webdriver.Chrome()
query = "mobile"
file = 0

#Loops through the first 19 pages of search results.
for i in range(1,20):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")

    #Finds all elements matching the class name _75nlfW.
    elems = driver.find_elements(By.CLASS_NAME, "_75nlfW")
    #Prints the number of items found on the page.
    print(f"{len(elems)} items found")
    print(elems)
    for elem in elems:
        #Saves the HTML content of each element to separate .html files in a folder named data.
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html","w", encoding="utf-8") as f:
            f.write(d)
            file +=1
    print(elem.text)

    time.sleep(2)
driver.close()