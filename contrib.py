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
            if row[24] in names_to_money:
                money = names_to_money[row[24]]
                money += abs(float(row[7]))
                names_to_money[row[24]] = money
            else:
                names_to_money[row[24]] = abs(float(row[7]))
        elif row[25][0] == 'C':
            if row[25] in names_to_money:
                money = fec_to_money[row[25]]
                money += abs(float(row[7]))
                fec_to_money[row[25]] = money
            else:
                fec_to_money[row[25]] = abs(float(row[7]))

ie_to_money= dict()
for fec in recipients.keys():
    if fec in fec_to_money:
        money = fec_to_money[fec]
        id = recipients[fec]
        ie_to_money[id] = money
names = open('names_to_ids.json')
name_to_id = json.load(names)
for name, ids in name_to_id.iteritems():
   for id in ids:
       iemoney = ie_to_money.get(id,0)
       names_to_money[name] += iemoney

def get_sorted_ids():
    sortednames = sorted(names_to_money.items(), key=itemgetter(1))
    sorted_ids = [ (name_to_id[x],y) for x,y in sortednames if x in name_to_id]
    return sorted_ids
