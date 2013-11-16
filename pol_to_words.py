from secrets import Secrets
import contrib as Contrib

import urllib2 
import json
import heapq

class PoliticiansToWords:
    api_key = Secrets.sunlight_key
    
    @classmethod
    def get_words_from_politician(cls, politician_id):
        request_uri = 'http://capitolwords.org/api/1/phrases.json?entity_type=legislator&entity_value=' + str(politician_id) + '&apikey=' + str(cls.api_key)

        response = urllib2.urlopen(request_uri)
        words = json.loads(response.read())
        
        return [(word['count'], word['ngram']) for word in words]

    #returns number of times a congressperson has used the word, given the bioguide id
    @classmethod
    def get_politician_count(cls,word,politician_id):
        request_uri = 'http://capitolwords.org/api/1/text.json?phrase='+str(word)+'pharmaceutical&bioguide_id=' + str(politician_id) +'&apikey' + str(cls.api_key)
        response = urllib2.urlopen(request_uri)
        
        words = json.loads(response.read())
        return words['num_found']

    @classmethod
    def get_frequencies(cls, top_word_list, politician_list):
        frequencies = []
        for politican in politician_list:
            sum = 0
            for word in top_word_list:
                sum += PoliticiansToWords.get_politician_count(word,politician)
            frequencies.append((politician,sum))
        return frequencies

    # returns top N words from total of politician ids, or 0 for all
    @classmethod
    def top_words(cls, politician_ids, n=20):
        words = dict()

        for pol_id in politician_ids:
            top_pol = cls.get_words_from_politician(pol_id)

            for count, word in top_pol:
                words[word] = count + words.get(word, 0)

        blacklist = ['going', 'think', 'percent', 'floor', 'friend', 'leader', 'side', 'court', 'lot', 'really', 'gentlewoman', 'san', 'actually', 'fact', 'ought', 'talking', 'basically', 'drugs', 'taxes', 'republican', 'democrats']
        for word in blacklist:
            if word in words:
                words.pop(word)

        top = [(count, word) for word, count in words.iteritems()]
        heapq.heapify(top)

        if n == 0:
            n = len(top)

        return heapq.nlargest(n, top)


#bioguide_to_ie.csv
def id_to_bioid():
    import csv

    mapping = dict()

    with open('bioguide_to_ie.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            mapping[row[1]] = row[0]

    return mapping

id_list = Contrib.get_sorted_ids()
id_list = [x for x,y in id_list[-53:-3]]
id_list = [y for x in id_list for y in x]

bioids = set()
mapping = id_to_bioid()
for id in id_list:
    if id in mapping:
        bioids.add(mapping[id])
    else:
        pass


words = PoliticiansToWords.top_words(list(bioids), 50)
#took out more words
words = ['health', 'tax', ' president', 'care', 'medicare', 'consent', 'insurance', 'unanimous', 'budget', 'drug', 'energy', 'rights', 'law', 'majority', 'education', 'seniors', 'oil', 'prescription', 'nuclear', 'patients', 'plan', 'debt', 'research', 'water', 'cancer', 'benefit']

