from secrets import Secrets

import httplib

class PoliticiansToWords:
    api_key = Secrets.sunlight_key
    
    @classmethod
    def get_words_from_politician(cls, politician_id):
        request_uri = 'http://capitolwords.org/api/1/phrases.json?entity_type=legislator&entity_value=' + str(politician_id) + '&apikey=' + str(cls.api_key)

        return "test"
    

     
     
print PoliticiansToWords.get_words_from_politician('test')
