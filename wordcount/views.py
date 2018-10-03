from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for i in wordlist:
        if i in worddict:
            worddict[i] += 1
        else:
            worddict[i] = 1
    # We use .items() to turn the dict into a list
    sortedwords = sorted(worddict.items(), key=itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})
