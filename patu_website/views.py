from django.shortcuts import render


# method view
def index_home(request):
    context = {
        'title': 'Patu Website',
        'author': 'Patu',
        'date_copyright': '2020',
        'link': 'pornhub.com'
    }
    return render(request, 'index.html', context)
