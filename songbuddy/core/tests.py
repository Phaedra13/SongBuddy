from django.test import TestCase
import requests
import json
# Create your tests here.
def getRhymes():

    datamuse_url = f'https://api.datamuse.com/words?rel_rhy=hello'

    response = requests.get(datamuse_url)

    return response.json()
print(type(json.dumps(getRhymes())))
