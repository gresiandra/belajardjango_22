from django.shortcuts import render
from .form import wordcountForm

def index(request):

    # panggil form dari form.py
    wordForm = wordcountForm(request.POST or None)

    # deklarasi list
    fulltextdivide = []

    # deklarasi dictionary
    worddict = {}
    sorteddict = {}

    if request.method == 'POST':
        fulltext = request.POST['words']
        fulltextdivide = fulltext.split()
        
        for word in fulltextdivide:
            if word in worddict:
                # tambah value dictionary
                worddict[word] += 1
            else:
                # masukan dalam dictionary
                worddict[word] = 1
        
        sorteddict = sorted(worddict.items(), key=lambda x: x[1], reverse=True)[:7]

    context = {
        'title':'WordCount Project',
        'wordForm':wordForm,
        'textlength': len(fulltextdivide),
        'sorteddict':sorteddict
    }
    return render(request, 'index.html', context)
