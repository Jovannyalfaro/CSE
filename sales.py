import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    fruits = 0
    clothes = 0
    meat = 0
    beverages = 0
    office_supplies = 0
    cosmetics = 0
    snacks = 0
    personal_care = 0
    house_hold = 0
    vegetables = 0
    baby_food = 0
    cereal = 0
    print("processing.....")
    for row in reader:
        if row[2] == "Cosmetics":
            profits = float(row[13])
            for i in row[13]:
                cosmetics += 1
    for row in reader:
        if row[2] == "fruits":
            profits = float(row[13])
            for i in row[13]:
                fruits += 1
    for row in reader:
        if row[2] == "clothes":
            profits = float(row[13])
            for i in row[13]:
                clothes += 1
    for row in reader:
        if row[2] == "beverages":
            profits = float(row[13])
            for i in row[13]:
                beverages += 1
    for row in reader:
        if row[2] == "office_supplies":
            profits = float(row[13])
            for i in row[13]:
                office_supplies += 1
    for row in reader:
        if row[2] == "snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += 1
    for row in reader:
        if row[2] == "personal_care":
            profits = float(row[13])
            for i in row[13]:
                personal_care += 1
    for row in reader:
        if row[2] == "house_hold":
            profits = float(row[13])
            for i in row[13]:
                house_hold += 1
    for row in reader:
        if row[2] == "house_hold":
            profits = float(row[13])
            for i in row[13]:
                house_hold += 1
    for row in reader:
        if row[2] == "house_hold":
            profits = float(row[13])
            for i in row[13]:
                house_hold += 1
    for row in reader:
        if row[2] == "house_hold":
            profits = float(row[13])
            for i in row[13]:
                house_hold += 1
    for row in reader:
        if row[2] == "vegetables":
            profits = float(row[13])
            for i in row[13]:
                vegetables += 1
    for row in reader:
        if row[2] == "baby_food":
            profits = float(row[13])
            for i in row[13]:
                baby_food += 1
    for row in reader:
        if row[2] == "cereal":
            profits = float(row[13])
            for i in row[13]:
                cereal += 1
print("The profits for fruits is %d" % fruits)
print("The profits for vegetables is %d" % vegetables)
print("The profits for cereal is %d" % cereal)
print("The profits for house_hold is %d" % house_hold)
print("The profits for baby_food is %d" % baby_food)
print("The profits for beverages is %d" % beverages)
print("The profits for personal_care is %d" % )
print("The profits for  is %d" % )
print("The profits for  is %d" % )
print("The profits for  is %d" % )
print("The profits for  is %d" % )
print("The profits for  is %d" % )