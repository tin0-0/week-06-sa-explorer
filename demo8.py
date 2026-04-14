import re
pattern = r"0\d{9}"
text = "Call 0823456789 or 0712345678 for support."

matches = re.findall(pattern,text)
print(matches)