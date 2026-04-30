#method 1: read entire file
f =open("provinces.txt", "r")
content = f.read()
print(content)
f.close()
#method 2: read lines 
f=open("provinces.txt", "r")
for line in f:
    print(line.strip())
f.close()