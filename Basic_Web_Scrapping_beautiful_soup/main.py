
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
    print(content)

# using beautiful library to pretify the html file to use different tags 