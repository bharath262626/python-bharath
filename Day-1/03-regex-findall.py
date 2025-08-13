import re

text = "The quick white fox"
pattern = r"brown"

search = re.search(pattern, text)

if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")

     
