from secrets import Secrets

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

    # returns top N words from total of politician ids
    def top_words(cls, politician_ids, n=20):
        words = dict()

        for pol_id in politician_ids:
            top_pol = PoliticianToWords.get_words_from_politician(pol_id)

            for count, word in top_pol:
                words[word] = count if not words[word] else count + words[word]     
    

        top = heapify([(count, word) for count, word in words])

        return heapq.nlargest(n, top)

     
     
PoliticiansToWords.get_words_from_politician('L000551')
