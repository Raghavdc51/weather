from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    
    city=request.GET.get('city')
    
    api_key="3f9602eda3681f64a6fa1d30b5a77ead"
    
    api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    print(api_url)
    
    api =requests.get(api_url).json()
    
    temperature=api["main"]["temp"]
    
    city=api["name"]
    
    country=api['sys']['country']
    
    return render(request,'index.html',{'temperature':temperature 
    ,'city':city, 'country':country})