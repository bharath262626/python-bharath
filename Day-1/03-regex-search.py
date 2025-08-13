import re 

text = "The text is super challenging"
pattern = r"talent"

search = re.search(pattern, text)
if search:
    print("if success search:", search.group())
else: 
    print("does nt print")
    