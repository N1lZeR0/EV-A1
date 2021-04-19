import cli_ui #imports cli-ui module for gui like feature in command  line
import time #imports time module
cli_ui.info_progress(">>Acessing Data ..... ", 0, 100) #Shows progress of "Acessing Data", just for show
cli_ui.info_progress(">>Acessing Data ..... ", 10, 100)
time.sleep(4)
cli_ui.info_progress(">>Acessing Data ..... ", 35, 100)
time.sleep(5)
cli_ui.info_progress(">>Acessing Data ..... ", 54, 100)
time.sleep(3)
cli_ui.info_progress(">>Acessing Data ..... ", 99, 100)
time.sleep(1)
cli_ui.info_progress(">>Acessing Data ..... ", 100, 100)
print("")
print(">>AI Founded: EVA.AI")
print(">>Intiating AI.....")
time.sleep(4)
print("{                     EVA                        }")
print("")
print("EVA Sucessfully initiated")
print("")
time.sleep(2)
def Gender(): #creates a Gender module to tell program whether you are a girl or boy
  GE = ["sir", "madam"]
  g = input('You are a sir or a madam: ')
  time.sleep(1)
  while True: #A while loop thats ensure the loop goes on and on incase of wrong input
    if g == "sir":
      print('Hello, ' + g)
      break
    elif g == "madam":
      print('Hello, ' + g)
      break
    else:
      print("Please enter correct one")
      Gender()
      break
Gender() #intializes Gender function
user = input('Enter your user name here: ') #enter your name here
print("Hello, " + user)
time.sleep(2)
print( "Hello, I am EVA, Your Educational Virtual Assistant.")
print( "I can help you in studies.")
print( "To ask question, type questions")
print( "To download videos, type youtube")
print( "To see time, type clock")
print( "To see the weather, type weather")
print( "To translate words and phrases, type translator")
import  requests, json
def translator(): #creates a translator module
  while True:
    print("This is Google Translate, Python Editon")
    print("Here are the languages that are supported. ")
    import google_trans_new #import google translator module for translation
    import time
    print(google_trans_new.LANGUAGES) #shows all the languages supported by the translator
    ex = input('If you got the language you want, then press i')
    print("Language code is the short form of langauge, for example English-en, Odia- or. ")
    distlang = input("Enter the code language here:- ")
    source =input("Enter the word or phrase you want to translate:- ")
    from google_trans_new import google_translator
    translator = google_translator()
    result = translator.translate(source, lang_tgt = distlang) #translates the input in english to another language
    print("This is the translated word or phrase:-" + result)
def questions(): #creates a function for wikipedia
    import wikipedia #imports wikipedia module
    from googlesearch import search #imports google search for searching
    while True: #creats a endless while loop
        my_input = input('You can ask your question here :') # Takes a input from user as a question
        try:
            print(wikipedia.summary(my_input)) #prints the summery from wikipedia
            print("")
            print("or")
            print("if you want to get more information, then search urls given below")
            query = my_input
            for p in search (query,  tld='co.in', num=6, stop=6, pause=6):
                print(p) #prints the related url
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        except:
            print('')
def clock(): #A clock function to see the time
    import datetime #imports datetime
    import pytz #imports pytz
    while True:
        try:
            current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            print("the current time is : ", current_time, end='\r', flush=True) #prints the current time in one line
        except:
            print('') #shows nothing instead of a long error
def youtube(): #creates a youtube function for downloading videos
    import youtube_dl #imports youtube dl for youtube downloader
    while True:
        ydl_opts = {}
        def dwl_vid():
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                  ydl.download([zxt])
        channel = 1
        while (channel == int(1)):
            link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download:- ") #takes link as input
            zxt = link_of_the_video.strip()
            dwl_vid() #downloads the video
            channel = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done "))
def weather(): #imports weather function for viewing weather
    while True:
        api_key = "311f77f88982535affa17f4ba1c5e8da"
        base_url =  "http://api.openweathermap.org/data/2.5/weather?"
        city_name = input("Please enter the city name. ") #takes city name from user
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name #gets the complete url
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " + str(current_temperature) + "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))
def comms(): #creates a funtion to call other function
  INP = ["questions", "youtube", "clock", "weather", "translator"]
  inputi = input("Type the command here. ")
  while True:
    if  inputi == "questions":
      questions()
      break
    elif inputi == "youtube":
      youtube()
      break
    elif inputi == "clock":
      clock()
      break
    elif inputi == "weather":
      weather()
      break
    elif inputi == "translator":
      translator()
      break
    else:
      print("Please enter correct command.")
      comms()
      break
comms()
