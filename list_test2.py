ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
total = 0
for num in range(len(ages)):
    total += ages[num]
average = total/len(ages)

print("The average of this list is:","{:<.2f}".format(average))
