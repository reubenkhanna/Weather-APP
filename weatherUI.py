"""
Weather application which takes in city as input and gets the weather using pyowm
@AUTHOR: Utkarsh Reuben Khanna
@CNO: C0750077
"""
#------Imports-----------------------------------------------------------------------------------------------------------------#
from tkinter import *
from tkinter import messagebox
import pyowm
from owk import KEY
#------------------------------------------------------------------------------------------------------------------------------#

#------Root--------------------------------------------------------------------------------------------------------------------#
top = Tk()                                                      #Intializing a TK object
top.geometry("425x350")                                         #Setting default height and width of Weather app
top.configure(background='#4A0C1E')                             #Adding background colour
#------------------------------------------------------------------------------------------------------------------------------#

#------Labels Config-----------------------------------------------------------------------------------------------------------#
L1 = Label(top, text = "Weather App", font=("Arial Bold", 20), fg="#DA8459", bg='#4A0C1E')      #Header Label
L1.pack( side = TOP)                                                                            #Specifies the location of Header
L1 = Label(top, text = "Enter City Name", font=("Arial", 10), fg="#DA8459", bg='#4A0C1E')       #Label for entry box
L1.pack( side = LEFT)                                                                           #Location for it                
L1.place(x=50, y=50)                                                                            #places on exact x andy coordinate 
L2 = Label(top, text = "Temperature in Celsius", font=("Arial", 15), fg="#DA8459", bg='#4A0C1E')   #Label for celsius 
L2.pack( side = LEFT)                                                                                 
L2.place(x=50, y=200)                                                                                #places on exact x andy coordinate 
L3 = Label(top, text = "Temperature in Fahrenheit", font=("Arial", 15), fg="#DA8459", bg='#4A0C1E') #Label for fahrenheit
L3.pack( side = LEFT)                       
L3.place(x=50, y=250)                                                                               #places on exact x andy coordinate 
L4 = Label(top, text = "0°C", font=("Arial", 15), fg="#967B42", bg='#4A0C1E')                       #Label for celsius temperature  
L4.pack( side = LEFT)                                                                           
L4.place(x=300, y=200)                                                                              #places on exact x andy coordinate 
L5 = Label(top, text = "0°F", font=("Arial", 15), fg="#967B42", bg='#4A0C1E')                       #Label for fahrenheit temperature
L5.pack( side = LEFT)                               
L5.place(x=300, y=250)                                                                              #places on exact x andy coordinate 
#-------------------------------------------------------------------------------------------------------------------------------#

#-----Entry config----------------------------------------------------------------------------------------------------------------#
E1 = Entry(top, bd=2)                                                                              #Entry object
E1.pack(side = RIGHT)                                                                              #Position to be placed at
E1.place(x=250, y=50)                                                                              #placed on exact x and y coordinate
#---------------------------------------------------------------------------------------------------------------------------------#

#------Temperature function--------------------------------------------------------------------------------------------------------#
def getTemperature(event):
    
    if E1.get() == "":       #Checks if the entry is blank
        messagebox.showinfo("Error", "Please enter city name") #shows error to user
    else:
        try:
            city = E1.get()      #get the city name entered by user 
            owm = pyowm.OWM(KEY) # get access using key
            observation = owm.weather_at_place(city) # get a json observation
            weather = observation.get_weather() # get the weather component

            temperature = weather.get_temperature('celsius') # get the celsius temperature
            L4['text'] = str(temperature['temp']) +" °C"     # set the celsius temperature to L4
        
            temperature = weather.get_temperature('fahrenheit') # get the fahrenheit temperature
            L5['text'] = str(temperature['temp']) + " °F"       # set the fahrenheit temperature  to L5
        except:
            messagebox.showinfo("Error", "Something went wrong we are unable to find what you are looking for") #shows error to user




def onClick():  #on click method to handle button click
    getTemperature("click")     #call the get temperature method with click event
    
BUTTON = Button(top, text="Get Weather", command=onClick,relief=RAISED, fg='#DA8459', bg="#501111", width=17) #Creates a button object
BUTTON.pack()                                                                                                 
BUTTON.place(x=250, y=100)                                                                                    #places button on exact x and y coordinate 

top.bind('<Return>', getTemperature)                        #sets getTemperature to be called when user hits enter 
  
top.mainloop()
