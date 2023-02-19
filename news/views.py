from django.shortcuts import render
import requests
urlapi = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=979b283611e44571805eeaed2b9bec1f')

# Create your views here.


def index(request):
    r = requests.get(urlapi)
    res = r.json()
    articles = res['articles']
    title = []
    description = []
    image = []
    url = []
    for i in articles:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['urlToImage'])
        url.append(i['url'])
    
    news = zip(title,description,image,url)

    context = {'news': news}
    return render(request, 'news/index.html', context)
