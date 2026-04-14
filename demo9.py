import re

text = "Call 0823456789 or 0712345678 for support."

#find all matches
digits = re.findall(r"\d+",text)
print(digits)

#Find the first match
m = re.search(r"\d{4}",text)
if m:
    print(f"First 4-digit number: {m.group()}" )

#Check if string MATCHES a pattern from the start
print(re.match(r"Order",text))
print(re.match(r"Confirmed",text))

# \d = any digit (0-9)
# \D = any NON-digit
# \w = any word character (letter, digits, underscore)
# \W =
#  c
# 
# 
#  
#match a, b or c 
pattern1 = r"[abc]"

#match any vowel
pattern2 = r"[aeiou]"

#match any digit (as \d)
pattern3 = r"[0-9]"

#match any letter (upper or lower)
pattern4 = r"[a-zA-Z]"

#not a digit
pattern5 = r"[^0-9]"

# + = one or more
# * = zero or more
# ? = zero or one (optional)
# {n} = exactly n 
# {n,m} = between n and m

text = "Order 42, total R1234.56, paid 2026-04-14"
print(re.findall(r"\d{4}", text))
print(re.findall(r"\d{1,}",text))

#phone must start with 0 and have exactly 10 digits TOTAL
pattern = r"^0\d{9}$"

print(bool(re.match(pattern, "+27834499819")))

"Born on 15/03/2006 in SA"
pattern = r"\d{2}/\d{2}/\d{4}"
patternID = r"^\d{13}$"

text = "Visit Cape Town and Durban"
matches = re.findall(r"\b[A-Z]\w+",text)
print(matches)