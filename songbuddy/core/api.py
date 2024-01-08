import requests
from rest_framework import status
from rest_framework.response import Response



def getRhymes(word,syllable_count):
    rhymebrain_url = f'https://rhymebrain.com/talk?function=getRhymes&word={word}'
    rhyme_words = requests.get(rhymebrain_url).json()
    rhyme_words_filtered = [entry['word'].capitalize() for entry in rhyme_words if entry['syllables'] == syllable_count]
    sorted_rhymes = sorted(rhyme_words_filtered)
    rhyme_string = ", ".join(sorted_rhymes)
    return rhyme_string

def getNearRhymes_match(word):
    rhymebrain_url = f'https://rhymebrain.com/talk?function=getRhymes&word={word}'
    near_rhyme_words = requests.get(rhymebrain_url).json()
    near_rhyme_score_sort = [entry for entry in near_rhyme_words if entry['score'] >= 300]
    near_rhymes_freq_sort = sorted(near_rhyme_score_sort, key=lambda entry: entry['freq'], reverse=True)
    near_rhymes_list = [entry['word'].capitalize() for entry in near_rhymes_freq_sort]
    return near_rhymes_list

def getNearRhymes_noMatch(word):
    rhymebrain_url = f'https://rhymebrain.com/talk?function=getRhymes&word={word}'
    near_rhyme_words = requests.get(rhymebrain_url).json()
    near_rhyme_score_sort = [entry for entry in near_rhyme_words if entry['score'] < 300]
    near_rhymes_freq_sort = sorted(near_rhyme_score_sort, key=lambda entry: entry['freq'], reverse=True)
    near_rhymes_list = [entry['word'].capitalize() for entry in near_rhymes_freq_sort]
    return near_rhymes_list

def thesaurus(word):
    apininjas_url = f'https://api.api-ninjas.com/v1/thesaurus?word={word}'
    synonym_words = requests.get(apininjas_url, headers={'X-Api-Key': 'QYWdoNYLPl+7Uizu4Q+qqw==pAUlFv9FYT8vJexR'}).json()
    synonym_list = synonym_words.get('synonyms', [])
    capitalized_synonyms = [synonym.capitalize() for synonym in synonym_list]
    synonym_string = ", ".join(capitalized_synonyms)
    return synonym_string

def similarSounding(word):
    datamuse_url = f'https://api.datamuse.com/words?sl={word}'
    similar_words = requests.get(datamuse_url).json()
    similar_words_list = sorted([entry['word'].capitalize() for entry in similar_words])
    similar_string = ", ".join(similar_words_list)
    return similar_string

# def getDefinition(word):
#     dictionaryapi_url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
#     definition = requests.get(dictionaryapi_url).json()
#     definition_filtered = [entry.get('meaning') for entry in definition]
#     return definition_filtered


