from django.http import HttpResponse
from . import htmlGenerator
minRange=3
maxRange=10
def game(request) :
    def minMax(x):
        x=int(x)
        if(x in range(minRange,maxRange+1)):
            return x
        elif(x>maxRange):
            return maxRange
        else:
            return minRange
    try:
        url=request.GET.get("d","4*4")
        if("*" in url):
            l,b = [minMax(x) for x in url.split("*")]
        else:
            l ,b= [minMax(url)]*2
    except:
        l,b=4,4
    return HttpResponse(htmlGenerator.htmlGenerator(l,b))