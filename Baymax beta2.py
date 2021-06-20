from tkinter import *
import webbrowser
import time
import sys

total_breaks = 3
break_count = 0

while True:
    time.sleep(5)
    root = Tk()
    root.title("BAYMAX")
    root.iconbitmap(' ') #specify icon location


    def soundcloud():
        webbrowser.open("https://soundcloud.com/relaxdaily/relaxing-music-calm-studying-yoga")


    def youtube():
        webbrowser.open("https://www.youtube.com/watch?v=r3fE6FQT82s")


    def medic():
        webbrowser.open("https://www.onlinecounselling4u.com")


    def kill():
        global break_count
        break_count += 1
        if break_count > total_breaks:
            sys.exit()

        root.destroy()


    def out():
        sys.exit()


    welcome = Label(root,
                    text="Hai..SHIBILY\nI am Baymax..\nYour personal buddy :)\nIt came to my attention that you have been using this computer for the past 2 hours continuosly...\nWould you like me to suggest something just to take a break?")
    welcome.pack()

    soundcloud = Button(root, text=" Open soundcloud and play some good relaxing music", command=soundcloud, fg="white",
                        bg="blue")
    youtube = Button(root, text=" Play some relaxing Youtube video", command=youtube, fg="white", bg="blue")
    medic = Button(root, text="Seek medical attention", command=medic, fg="white", bg="blue")
    Later = Button(root, text="Remind me later", command=kill, fg="white", bg="blue", )
    Exit = Button(root, text="Exit", command=out, fg="white", bg='red')

    soundcloud.pack()
    youtube.pack()
    medic.pack()
    Later.pack()
    Exit.pack()

    root.mainloop()