import requests
from rest_framework import status
from rest_framework.response import Response




def getRhymes(word):
    datamuse_url = f'https://api.datamuse.com/words?rel_rhy={word}'
    response = requests.get(datamuse_url)
    return response.json()

