import webbrowser
import time


while True:
     query = input('Hey ASH, I am Baymax\nYour personal buddy :)\nWould you like me to play some music?')
     Fl = query[0].lower()
     if query == '' or not Fl in ['y','n']:
        print('Please answer with yes or no!')
     else:
        break
if Fl == 'y':
    time.sleep(2)
    print("Wow let me open soundcloud and play some good relaxing music")
    webbrowser.open("https://soundcloud.com/relaxdaily/relaxing-music-calm-studying-yoga")
if Fl == 'n':
    time.sleep(2)
while True:
     query = input('Would you like me to play some relaxing Youtube video?')
     Fl = query[0].lower()
     if query == '' or not Fl in ['y','n']:
        print('Please answer with yes or no!')
     else:
        break
if Fl == 'y':
    time.sleep(2)
    print("Wow let me open Youtube and play some good music")
    webbrowser.open("http://www.youtube.com/watch?v=YXw16RzMofo")
if Fl == 'n':
    time.sleep(2)
    while True:
        query = input('Would you like me to seek medical attention?')
        Fl = query[0].lower()
        if query == '' or not Fl in ['y', 'n']:
            print('Please answer with yes or no!')
        else:
            break
if Fl == 'y':
    time.sleep(2)
    print("Ok let me open Online Counselling free4u ")
    webbrowser.open("https://www.onlinecounselling4u.com")
if Fl == 'n':
    time.sleep(2)
print("Ohh,please take a walk,You have been using the computer for the past 2 hour")
