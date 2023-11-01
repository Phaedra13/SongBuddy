from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from .api import getRhymes

def index(request):
    return render(request, "core/index.html")



def results(request):
    word = request.GET.get('word')
    #word from index.html
    rhymes_data = getRhymes(word)
    #rhymes_data from api
    context = {
        'rhymes': rhymes_data,
        #rhymes is what we replace in results.html
        #rhymes_data is what we replace it with, which we got from the api
        'word': word
    }
    return render(request, 'core/results.html', context)
 
 



