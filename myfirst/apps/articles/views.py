from django.http import HttpResponse

def index(request):
	return HttpResponse("Привет мир!")

def test(request):
	return HttpResponse("ТЕСТОВАЯ СТРАНИЦА")
# Create your views here.
