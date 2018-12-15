import csv

response = input("Type your feeling:")

with open("response.csv","w", newline='') as f:
    r = csv.writer(f, delimiter=",")
    
    r.writerow(response)
