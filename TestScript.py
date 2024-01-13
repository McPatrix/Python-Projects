from bs4 import BeautifulSoup

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