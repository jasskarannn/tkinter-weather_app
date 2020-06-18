import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import requests,os,urllib.request

HEIGHT = 450
WIDTH = 650

# fe1f970bdaeb33b4d0fed52cf844f061
# api.openweathermap.org/data/2.5/forecast?q={city name},{state},{country code}&appid={your api key}

def test_function(entry):
    print('This is the entry : ',entry)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        temp_min = weather['main']['temp_min']
        temp_max = weather['main']['temp_max']
        wind_speed = weather['wind']['speed']
        final_str = 'City : %s \n Conditions : %s\n Temperature (°C) : %s\n Minimum Temperature (°C) : %s\n Maximum Temperature (°C) : %s\n Wind Speed (Kmph) : %s' % (name,desc,temp,temp_min,temp_max,wind_speed)
    except:
        final_str = 'There was a problem retrieving information.\n Please try again.'

    return final_str


def get_weather(city):
    weather_key = 'fe1f970bdaeb33b4d0fed52cf844f061'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    
    parameters = {
        'APPID' : weather_key,
        'q' : city,
        'units' : 'Metric',
    } 

    response = requests.get(url, params=parameters)
    # print(response.json()) # json converts result into python dictionary

    weather = response.json()

    # print('The city name is : ',weather['name'])
    # print('Current Description : ',weather['weather'][0]['description'])
    # print('The current weather in Celcius Scale is : ',weather['main']['temp'])

    label['text'] = format_response(weather)


root = tk.Tk()
root.title('Weather App')

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open("/Users/gpsingh/Desktop/misc/TCP Python/weather-app/lake_hills.png",'r'))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0,relx=0,rely=0)

label1 = tk.Label(root, text='Welcome to the weather app.\n Type in the city or zipcode to retrieve the weather conditions.',bg='white',font='Verdana 17 italic')
label1.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.1)

frame = tk.Frame(root, bg ='#80c1ff')
frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame,text='Get Stats',font ='Courier 14 bold')
entry.place(relx=0.02,rely=0.30,relwidth=0.6,relheight=0.45)

button = tk.Button(frame, text='Get Weather', font ='Courier 14 bold',highlightbackground='#80c1ff',command=lambda: get_weather(entry.get()))
button.place(relx=0.65,rely=0.17,relwidth=0.3,relheight=0.7)

lower_frame = tk.Frame(root, bg ='#80c1ff')
lower_frame.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.50, anchor ='n')

label = tk.Label(lower_frame,font='Courier 16 italic',anchor='nw',justify='left',bd ='4')
label.place(relwidth=1, relheight=1)

day = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13n.png', '50d.png']
night = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']

base_url = 'https://openweathermap.org/img/w/'
img_dir = './img/'

if not os.path.exists(img_dir):
	os.makedirs(img_dir)

# Get the day weather icons
for name in day:
	file_name = img_dir+name
	if not os.path.exists(file_name):
		urllib.request.urlretrieve(base_url+name, file_name)

# Repeat the same thing for night weather icons
for name in night:
	file_name = img_dir+name
	if not os.path.exists(file_name):
		urllib.request.urlretrieve(base_url+name, file_name)


root.mainloop()