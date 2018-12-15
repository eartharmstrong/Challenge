import csv

movies = [["Top Gun", "Risky Buniness", "Minority Report"], ["Titanic",
           "The Revena", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movies_list.csv", "w") as f:
    w = csv.writer(f,delimiter = ",")
    for row in movies:
        w.writerow(row)


