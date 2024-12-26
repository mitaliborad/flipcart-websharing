from bs4 import BeautifulSoup
import pandas as pd
import os

d = {'title':[],'price':[],'link':[]}

for file in os.listdir("data") :
    try:
        with open (f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')

        product = soup.find("div", class_="tUxRFH")
        if product:
            link_tag = product.find("a", class_="CGtC98")
            if link_tag:
                title = link_tag.find("div", class_="KzDlHZ").get_text()  #product title
                link = "https://www.flipkart.com" + link_tag["href"]  #product link

        p = soup.find("div",attrs={"class" : 'Nx9bqj _4b5DiR'})
        price = (p.get_text())
        print("Title:", title)
        print("Price:", price)
        print("Link:", link)

    except Exception as e:
        print(e)

df = pd.DataFrame(data = d)
df.to_csv("data.csv")

    #print(soup.prettify())
