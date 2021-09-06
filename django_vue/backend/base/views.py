from django.shortcuts import HttpResponse

# Create your views here.
def ping(request):
    return HttpResponse("ping")