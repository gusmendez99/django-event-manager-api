from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the Home Page of Baby Events API. Try it out with Postman or CURL.</h1>")