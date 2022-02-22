from django.shortcuts import render

#return URL
def index_view (request):
    return render(request,'index.html')
