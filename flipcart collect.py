from bs4 import BeautifulSoup #use for parsing HTML & XML
import pandas as pd #for data collect in csv
import os # import os module in python

d = {'title':[],'price':[],'link':[]} # d creates dictionary with three keys 

for file in os.listdir("data") : # file in data folder
    try: # if in any file can't read link and title than ignore it

        with open (f"data/{file}") as f:# read every file in data folder
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser') 

        product = soup.find("div", class_="tUxRFH") # find  tUxRFH class
        if product:
            link_tag = product.find("a", class_="CGtC98") # find linktag in product
            if link_tag:
                title = link_tag.find("div", class_="KzDlHZ").get_text()  #find title in linktag
                link = "https://www.flipkart.com" + link_tag["href"]  #find link 

        p = soup.find("div",attrs={"class" : 'Nx9bqj _4b5DiR'}) # find price in Nx9bqj _4b5DiR class in new attribute
        price = (p.get_text()) # get_text = ignores the class and shows only text 
        print("Title:", title)
        print("Price:", price)
        print("Link:", link)

    except Exception as e:
        print(e)

df = pd.DataFrame(data = d) # with the help of pandas create dataframe of  data taken from d 
df.to_csv("data.csv")  # convert df into csv file 


