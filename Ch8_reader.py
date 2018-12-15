import csv

my_list = list()
with open("st.csv","r", newline='') as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
