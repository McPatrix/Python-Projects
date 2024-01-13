from bs4 import BeautifulSoup
import requests

# Open file
with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
# print(doc.prettify())

# Find by tag name

tag = doc.title
tag.string = "TESTTEST"
print(tag)

# Print string in tag

print(tag.string)

# This will find the only the first occurance 
tag2 = doc.find("a")
print(tag2)

# This will find ALL occurances
# Adding [] will find nested items

tag3 = doc.find_all("p")[0]
print(tag3)

# Using requests module

url = "https://www.newegg.com/msi-geforce-rtx-3080-rtx3080-suprim-x-10g/p/N82E16814137609?Item=9SIAPMXK7E6201"
#  Sends GET request to url variable 
result = requests.get(url)

# Prints text
#print(result.text)

# Parsing website HTML

doc2 = BeautifulSoup(result.text, "html.parser")
print(doc2.prettify())

# locate Text

prices = doc.find_all(str = "$")
print(prices)