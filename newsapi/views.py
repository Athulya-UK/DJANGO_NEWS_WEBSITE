from django.shortcuts import render
import requests
API_KEY='b375346fb3424667a4686ec7bc0d3845'
def home(request):
    country=request.GET.get('country')
    category=request.GET.get('category')
    everything=request.GET.get('everything')
    
    if country:
        a=country[0:2]
        print(a)
        url=f'https://newsapi.org/v2/top-headlines?country={a}&language=en&apikey={API_KEY}'
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
    elif category:
        url=f'https://newsapi.org/v2/top-headlines?category={category}&language=en&apikey={API_KEY}'
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
    elif everything:
        url=f'https://newsapi.org/v2/everything?q={everything}&from=2021-07-23&sortBy=popularity&language=en&apikey={API_KEY}'
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
    else:
        url=f'https://newsapi.org/v2/top-headlines?sources=bbc-news&language=en&apiKey={API_KEY}'
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
    
    context={
	    'articles':articles
    }
    return render(request,'newsapi/home.html',context)