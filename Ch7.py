list1 = [8, 19 ,148, 4]
list2 = [9, 1, 33, 83]
list3 = []

i = 0
for i in list1:
    for n in list2:
        list3.append(i*n)
print(list3)
