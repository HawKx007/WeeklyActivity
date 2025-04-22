from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title' : 'Aloha from PhoneReview'}
    return render(request, 'PhoneReview/index.html', context)