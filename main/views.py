from django.shortcuts import render
from .models import catalog
from .forms import wishesForm

def catalog_func(request):
    data = catalog.objects.all()
    title = 'Все произведения'

    if 'action_movie' in request.POST:
        data = catalog.objects.filter(genre = 'Боевик')
        title = 'Произведения по жанру боевик'
    elif 'romance' in request.POST:
        data = catalog.objects.filter(genre = 'Роман')
        title = 'Произведения по жанру роман'
    elif 'fantastic' in request.POST:
        data = catalog.objects.filter(genre = 'Фантастика')
        title = 'Произведения по жанру фантастика'
    elif 'history' in request.POST:
        data = catalog.objects.filter(genre = 'История')
        title = 'Произведения по жанру история'
    elif 'drama' in request.POST:
        data = catalog.objects.filter(genre = 'Драма')
        title = 'Произведения по жанру драма'
    elif 'comedy' in request.POST:
        data = catalog.objects.filter(genre = 'Комедия')
        title = 'Произведения по жанру комедия'

    return render(request, 'main/catalog.html', {'data': data, 'title': title})

def main(request):
    return render(request, 'main/main.html')

def wishes(request):
    error = ''
    complete = ''
    if request.method == 'POST':
        form_input = wishesForm(request.POST)
        if form_input.is_valid():
            form_input.save()
            complete = 'Форма успешно отправлена!'
        else: error = 'Форма неккоректно заполнена!'
    form = wishesForm()
    data = {'form': form, 
            'error': error,
            'complete': complete}
    return render(request, 'main/wishes.html', data)