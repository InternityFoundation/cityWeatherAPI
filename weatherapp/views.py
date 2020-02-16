
from django.shortcuts import render
#from  . weather import x
import requests, json 
from geopy import *

import requests, json 
import geocoder
from geopy import distance





def citydata(cityname):

    api_key = "d1ef724adff8128f87b72298791ad709"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "pune"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    print(complete_url)

    response = requests.get(complete_url) 

    x = response.json() 

    data=x
    return data


def index(request):

    print(request.GET) 

    if request.GET:#request.method == 'GET' :
        city=request.GET
        cityname=city["cityname"]



        api_key = "d1ef724adff8128f87b72298791ad709"

        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        city_name = cityname

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
        print(complete_url)

        response = requests.get(complete_url) 

        x = response.json() 






        g = geocoder.ip('me')

        mylocation=g.latlng
        lat=str(mylocation[0])
        lan=str(mylocation[1])

        # myweather= base_url + "appid=" + api_key + "?lat="+lat+"&lon="+lan
        # api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={your api key}

        myweather=base_url +"lat="+lat+"&lon="+lan+"&appid=" + api_key 
        print("latlan",lat,lan,"myweather",myweather)


        mydata = requests.get(myweather) 
        myweather_data=mydata.json() 
        print("latlan",lat,lan,"myweather",myweather_data)



        # data=x



        # def _fuzz_location(lat, lon, radius):
        # lat=139
        # log=35
        # radius=100
    
        # start = Point(lat, lon)
        # length = random.uniform(0, radius)
        # bearing = random.uniform(0, 360)

        # distance_vec = distance(meters=length)

        # new_pt = distance_vec.destination(start, bearing)
        # return new_pt.latitude, new_pt.longitude 





        
        center_point = [{'lat': -7.7940023, 'lng': 110.3656535}]
        test_point = [{'lat': -7.79457, 'lng': 110.36563}]
        radius = 5 # in kilometer

        center_point_tuple = tuple(center_point[0].values()) # (-7.7940023, 110.3656535)
        test_point_tuple = tuple(test_point[0].values()) # (-7.79457, 110.36563)

        dis = distance.distance(center_point_tuple, test_point_tuple).km
        print("Distance: {}".format(dis)) # Distance: 0.0628380925748918

        if dis <= radius:
            print("{} point is inside the {} km radius from {} coordinate".format(test_point_tuple, radius, center_point_tuple))
        else:
            print("{} point is outside the {} km radius from {} coordinate".format(test_point_tuple, radius, center_point_tuple))


        datamain=citydata(cityname)
        data=datamain["main"]
        print("data main",data)

        # print("new_pt>>",new_pt)
        return render(request,'index.html',{'data':data,'mylocation':mylocation})
    else:
        data="please  enter city name"
        return render(request,'index.html',{'data':data})

		

