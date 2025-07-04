import re

pattern = r"^abcd"
mystring = "abcdef"

x = re.match(pattern,mystring)
print(x)