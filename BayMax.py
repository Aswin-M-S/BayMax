import webbrowser
import time
import sys

total_breaks = 3
break_count = 0

while break_count < total_breaks:
    time.sleep(5)
    while True:
        query = input('Hai..Aswin\nI am Baymax..\nYour personal buddy :)\nIt came to my attention that you have been using this computer for the past 2 hours continuosly...\nWould you like me to suggest something just to take a break?')
        Fl = query[0].lower()
        if query == '' or not Fl in ['y', 'n']:
            print('Please answer with yes or no!')
        else:
            break
    if Fl == 'y':
        time.sleep(1)
        print("Wow let me open soundcloud and play some good relaxing music")
        webbrowser.open("https://soundcloud.com/relaxdaily/relaxing-music-calm-studying-yoga")
    if Fl == 'n':
        time.sleep(1)
        while True:
            query = input('Would you like me to play some relaxing Youtube video?')
            Fl = query[0].lower()
            if query == '' or not Fl in ['y', 'n']:
                print('Please answer with yes or no!')
            else:
                break
        if Fl == 'y':
            time.sleep(1)
            print("Wow let me open Youtube and play some good relaxing music video")
            webbrowser.open("https://www.youtube.com/watch?v=r3fE6FQT82s")
        if Fl == 'n':
            time.sleep(1)
            while True:
                query = input('Would you like me to seek medical attention?')
                Fl = query[0].lower()
                if query == '' or not Fl in ['y', 'n']:
                    print('Please answer with yes or no!')
                else:
                    break
            if Fl == 'y':
                time.sleep(1)
                print("Ok let me take you to OnlineCounsellingfree4u.com ")
                webbrowser.open("https://www.onlinecounselling4u.com")
                sys.exit()
            if Fl == 'n':
                time.sleep(1)
                print("Ohh kk...\nSo please take a walk,\nYou have been using the computer for the past 2 hours\nGo out and get some fresh air....Your Dear friend Baymax :)")
                break_count = break_count + 1
