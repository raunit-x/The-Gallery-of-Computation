from django.shortcuts import render


# Create your views here.
def home(request):
    context = {'page_title': 'Playground: The Gallery of Computation'}
    return render(request, 'playground/playground.html', context)
