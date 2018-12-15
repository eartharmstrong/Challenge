import re

string = "Two too."

m = re.findall("t[ow]",
               string,
               re.IGNORECASE)

print(m)
