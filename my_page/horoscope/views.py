from django.shortcuts import render
from django.http import HttpResponse

zodiak={
	'leo': 'Oven',
	'scorpio': 'Scorpio'
}
# Create your views here.
def leo(request):
	return HttpResponse("Лев")

def scorpio(request):
	return HttpResponse("Скорпион")

def get_info(request,zodiak):
	if zodiak=='leo':
		return HttpResponse("Leo")
	return HttpResponse(f"Your url: {zodiak}")