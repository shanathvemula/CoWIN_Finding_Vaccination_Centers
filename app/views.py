from django.shortcuts import render
import requests


# Create your views here.
def convert_date(s):
    l = s.split('-')
    k = l[2]+'-'+l[1]+'-'+l[0]
    return  k
def input(request):
    return render(request, 'index.html')
def index(request):
    age = 52
    pincode = str(request.GET['pin'])
    date = request.GET['date']
    date1 = convert_date(date)
    while True:
        counter = 0
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, date1)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        result = requests.get(URL,headers=header)
        rjson = eval(result.text)
        print(type(rjson))
        if result.ok:
            return render(request,'index.html',{'rjson':rjson})

def reg(request):
    return render(request, 'register.html')
