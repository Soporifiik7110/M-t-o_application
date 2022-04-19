import requests
import datetime as dt
from tkinter import *
from functools import partial

fenp = Tk()
fenp.geometry("800x500")
fenp.title("Météo application")
fenp.iconphoto(False, PhotoImage(file="bey.png"))
fond = Label(fenp,bg="#E8BA00")
fond.place(x=0, y=0, relheight=1, relwidth=1)
bandenoir = Label(fenp, bg="black")
bandenoir.place(x=0,y=0, width=800, height=55)
imerecherche = PhotoImage(file="buttonrecherche.png")
rechercheplace = Label(fenp, bg="white", borderwidth=0)
rechercheplace.place(x=290,y=45, height=1, width=200)

def cityname(car):
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        key = "c956f34308cf1ecb933aa5e907a01ac8"
        new = car.get()
        if new == "":
                return
        city = new
        lang = "fr"
        url = base_url + "appid=" + key + "&q=" + city + "&lang=" + lang
        ###############################
        def kelvin_to_celsuis_fahrenheit(kelvin):
            celsuis = kelvin - 273.15
            fahrenheit = celsuis * (9/5) + 32
            return celsuis, fahrenheit

        response = requests.get(url).json()
        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsuis_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsuis_fahrenheit(feels_like_kelvin)
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        weather1 = response['weather'][0]['main']
        vue_distance = response['visibility']
        nuage_pourcent = response['clouds']['all']
        pression = response['main']['pressure']
        #cache pour la température
        cache0 = Label(fenp, bg="#E8BA00")
        cache0.place(x=310, y=150, width=250, height=50)
        #Label pour la température
        temperature = Label(fenp, text=f'{temp_celsius:.1f}°C', font=("alfa slab one", 38, "bold", "italic"), fg='black', bg="#E8BA00")
        temperature.place(x=310, y=150)
        #################################################################################
        #cache pour la description
        cache1 = Label(fenp, bg="#E8BA00")
        cache1.place(x=269, y=210, width=235, height=40)
        # cache pour la longueur de la météo
        if len(description) > 10:
                #Label pour la méteo
                meteo1 = Label(fenp, text=f'{description}', font=("alfa slab one", 25, "bold", "italic"), fg='black',bg="#E8BA00")
                meteo1.place(x=290, y=210)
        else:
                meteo1 = Label(fenp, text=f'{description}', font=("alfa slab one", 25, "bold", "italic"), fg='black',bg="#E8BA00")
                meteo1.place(x=320, y=210)
        #cache pour la couche nuageuse
        cache3 = Label(fenp, bg="#E8BA00")
        cache3.place(x=100, y=342, width=55, height=25)
        #Label pour le poucentage de la couche nuageuse.
        couchenuage = Label(fenp, text=f'{nuage_pourcent}%', font=("alfa slab one", 14, "bold", "italic"), fg='black', bg="#E8BA00")
        couchenuage.place(x=100, y=342)
        #cache pour le vent
        cache2 = Label(fenp, bg="#E8BA00")
        cache2.place(x=310, y=342, width=50, height=25)
        #Label pour la vitesse du vent
        vitesseduvent= Label(fenp, text=f'{wind_speed*3.6:.2f}', font=("alfa slab one", 14, "bold", "italic"), fg='black', bg="#E8BA00")
        vitesseduvent.place(x=305, y=342)
        #label pour l'humiditée
        humiditeindic = Label(fenp, text=f'{humidity}', font=("alfa slab one", 14, "bold", "italic"), fg='black', bg="#E8BA00")
        humiditeindic.place(x=470, y=342)
        #label pour le baromètre
        baroindic = Label(fenp, text=f'{pression}', font=("alfa slab one", 14, "bold", "italic"), fg='black', bg="#E8BA00")
        baroindic.place(x=615, y=340)
        #background carré pour la chaleur
        temptest = f"{temp_celsius:.0f}"
        if float(temptest) > 20:
                cachep = Label(fenp, bg="#E8BA00")
                cachep.place(x=68, y=90, height=180, width=12)                               #zone a finir
                point1 = Label(fenp, bg="black")
                point1.place(x=68, y=120, width=10, height=10)

        if 10 < float(temptest) <= 20:
                cachep = Label(fenp, bg="#E8BA00")
                cachep.place(x=68, y=90, height=180, width=12)

                point1 = Label(fenp, bg="black")
                point1.place(x=68, y=170, width=10, height=10)

        if 0 < float(temptest) < 10:
                cachep = Label(fenp, bg="#E8BA00")
                cachep.place(x=68, y=90, height=180, width=12)
                point1 = Label(fenp, bg="black")
                point1.place(x=68, y=225, width=10, height=10)
##################################################################################################################################
car = StringVar()
passwordEntry = Entry(fenp, textvariable=car, font=("alfa slab one", 14, "bold", "italic"), fg="white", bg="black", borderwidth=0)
passwordEntry.place(x=300, y=20, width=200)
#################################################
cityname = partial(cityname, car)
#image pour le boutton de recherche de la ville
imboutton = PhotoImage(file="powerbutton.png")
loginButton = Button(fenp, text="", image=imboutton, command=cityname, bg='black', borderwidth=0)
loginButton.place(x=470, y=2, height=53)
#pour l'interface graphique
#imgae pour le pourcentage de nuage
cloudimage = PhotoImage(file="cloud.png")
cloudplace = Label(fenp, text="", image=cloudimage, bg="#E8BA00")
cloudplace.place(x=100, y=330)
#image pour la vitesse du vent
windimage = PhotoImage(file="wind.png")
windplace = Label(fenp, text="", image=windimage, bg="#E8BA00")
windplace.place(x=300, y=330)
#image pour l'humiditée
humideimage = PhotoImage(file="humidity.png")
humideplace = Label(fenp, text="",image=humideimage, bg="#E8BA00")
humideplace.place(x=430, y=320)
#image pour le baromètre
baroimage = PhotoImage(file="baromètre.png")
baroplace = Label(fenp, image=baroimage, bg="#E8BA00")
baroplace.place(x=630, y=320)
#pour l'interface de l'indice de la chaleur
chaleur30_20 = Label(fenp,bg="yellow")
chaleur30_20.place(x=50, y=90, height=60, width=10)
#de 20 a 10
chaleur20_10 = Label(fenp, bg="green")
chaleur20_10.place(x=50, y=150, height=60, width=10)
#de 10 a 0
chaleur10_0 = Label(fenp,bg="blue")
chaleur10_0.place(x=50, y=210, height=60, width=10)
#fin du programme
fenp.mainloop()