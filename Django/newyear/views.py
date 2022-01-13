from calendar import month
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.





def index(request):
   now = datetime.datetime.now()
   dateTimeNow = datetime.datetime.now().strftime("%d/%m/%Y")
   return render(request, "newyear/index.html", {
      "newyear": now.month == 1 and now.day == 1,
      "dateNow": dateTimeNow
})