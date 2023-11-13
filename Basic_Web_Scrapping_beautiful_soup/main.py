
from bs4 import BeautifulSoup
import os

# accessing the file 

# with open("test.html",'r') as test_file:
#     content = test_file.read()
#     print(content)

# os creates a platform independent file 
file_path = os.path.join("F:\Web_scrapping_projects\Web_scrapping_Projects\Basic_Web_Scrapping_beautiful_soup","test.html")

with open(file_path,"r") as html_file:
    content = html_file.read()
    # print(content)

# using beautiful library to pretify the html file to use different tags 

# creating an instance of beautiful soup 

    soup = BeautifulSoup(content,'lxml') 
# secondargumetn isto specify the parser method
# sincewe we want the content as strings used lxml parser to read html

# print(soup.prettify()) # exsactly like html 

# grabbing some tags from html pages



# tags = soup.find("h2")
# print(tags)



# we have to itterate through each h2 tags 

# find method: searches for the first instance of the <h2> tag to find all 
# we will simply use file_all method


    tags = soup.find_all("h2")

    for tag in tags:
        print(tag)
        # still we are getting tags , but we want only texts

    for tag in tags:
        print(tag.text)  # its msilib module in-built