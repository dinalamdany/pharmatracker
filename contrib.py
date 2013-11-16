import csv
recipients = dict()
with open('final_mapping_committee-to-entity.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile)
    for key,value in reader:
        recipients[key] = value
donations1 = dict()
donations2 = dict()
with open('contributions.csv','rU') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[25] == '':
                pass
        elif row[25][0] == 'N':
            try:
                money = donations2[row[24]]
                money += abs(float(row[7]))
                donations2[row[24]] = money
            except:
                donations2[row[24]] = abs(float(row[7]))
        elif row[25][0] == 'C':
            try:
                money = donations1[row[25]]
                money += abs(float(row[7]))
                donations1[row[25]] = money
            except:
                donations1[row[25]] = abs(float(row[7]))
mapped = dict()
for x in recipients.keys():
    try:
        money = donations1[x]
        id = recipients[x]
        mapped[id] = money
    except:
        pass