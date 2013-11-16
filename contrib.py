import json
from operator import itemgetter
import csv

recipients = dict()
with open('final_mapping_committee-to-entity.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile)
    for key,value in reader:
        recipients[key] = value

fec_to_money = dict()
names_to_money = dict()
with open('contributions.csv','rU') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[25] == '':
                pass
        elif row[25][0] == 'N':
            try:
                money = names_to_money[row[24]]
                money += abs(float(row[7]))
                names_to_money[row[24]] = money
            except:
                names_to_money[row[24]] = abs(float(row[7]))
        elif row[25][0] == 'C':
            try:
                money = fec_to_money[row[25]]
                money += abs(float(row[7]))
                fec_to_money[row[25]] = money
            except:
                fec_to_money[row[25]] = abs(float(row[7]))

ie_to_money= dict()
for x in recipients.keys():
    try:
        money = fec_to_money[x]
        id = recipients[x]
        ie_to_money[id] = money
    except:
        pass
names = open('names_to_ids.json')
name_to_id = json.load(names)
for name, ids in name_to_id.iteritems():
   for id in ids:
       iemoney = ie_to_money.get(x,0)
       names_to_money[name] += iemoney

sortednames = sorted(names_to_money.items(), key=itemgetter(1))
sorted_ids = [ (name_to_id[x],y) for x,y in sortednames if x in name_to_id]
