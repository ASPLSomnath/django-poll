from django.http import HttpResponse

def home(request):
    return HttpResponse(
        """Hello Django.  for more go to /polls , /polls/(1,2,3,4,5,6,7) , /polls/1/requests"""
)
