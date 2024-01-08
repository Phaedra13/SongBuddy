from django.http import HttpResponse
from django.shortcuts import render
from .api import getRhymes,getNearRhymes_match,getNearRhymes_noMatch,thesaurus,similarSounding

def index(request):
    return render(request, "core/index.html")


def results(request):
    word = request.GET.get('word')
    #word from index.html
    rhymes_data_one = getRhymes(word,'1')
    #rhymes_data from api
    rhymes_data_two = getRhymes(word,'2')
    rhymes_data_three = getRhymes(word,'3')
    rhymes_data_four = getRhymes(word,'4')
    rhymes_data_five = getRhymes(word,'5')
    rhymes_data_six = getRhymes(word,'6')
    rhymes_data_seven = getRhymes(word,'7')
    rhymes_data_eight = getRhymes(word,'8')
    rhymes_data_nine = getRhymes(word,'9')
    rhymes_data_ten = getRhymes(word,'10')
    near_rhymes_match_data = getNearRhymes_match(word)
    near_rhymes_no_match_data = getNearRhymes_noMatch(word)
    thesaurus_data = thesaurus(word)
    similar_sound_data = similarSounding(word)
    context = {
        'word': word.capitalize(),
        'one_rhymes': rhymes_data_one,
        'two_rhymes': rhymes_data_two,
        'three_rhymes': rhymes_data_three,
        'four_rhymes': rhymes_data_four,
        'five_rhymes': rhymes_data_five,
        'six_rhymes': rhymes_data_six,
        'seven_rhymes': rhymes_data_seven,
        'eight_rhymes': rhymes_data_eight,
        'nine_rhymes': rhymes_data_nine,
        'ten_rhymes': rhymes_data_ten,
        'near_rhymes_match': near_rhymes_match_data,
        'near_rhymes_no_match': near_rhymes_no_match_data,
        'synonyms': thesaurus_data,
        'similar_words': similar_sound_data,
        #rhymes is what we replace in results.html
        #rhymes_data is what we replace it with, which we got from the api
    }
    return render(request, 'core/results.html', context)

 



 