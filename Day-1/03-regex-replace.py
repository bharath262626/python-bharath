import re

text = "I am a super bad boy"
pattern = r"boy"

replacement = "girl"

new_text = re.sub(pattern, replacement, text)
print("modified text:", new_text)
