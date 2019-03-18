from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse


#create your views here
def index(request):
    return render(request, 'webapp/home.html')

def contact(request):
    return render(request, 'webapp/basic.html', {'content': ['hey reach me', '@ 8095179891']})