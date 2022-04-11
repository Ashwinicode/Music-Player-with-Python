from tkinter import *
import pygame
import tkinter as tkr
import os

root = Tk()  # In order to create an empty window
# Passing Root to MusicPlayer Class

        # Title of the window
root.title("My Music Player")
        # Window Geometry
root.geometry("1000x200+200+200")

def playsong():
            # Displaying Selected Song title
    root.track.set(root.playlist.get(ACTIVE))
            # Displaying Status
    root.status.set("-Playing")
            # Loading Selected Song
    pygame.mixer.music.load(root.playlist.get(ACTIVE))
            # Playing Selected Song
    pygame.mixer.music.play()


def stopsong():
            # Displaying Status
    root.status.set("-Stopped")
            # Stopped Song
    pygame.mixer.music.stop()


def pausesong():
            # Displaying Status
    root.status.set("-Paused")
            # Paused Song
    pygame.mixer.music.pause()

def unpausesong():
            # It will Display the  Status
    root.status.set("-Playing")
            # Playing back Song
    pygame.mixer.music.unpause()



        # Initiating Pygame
pygame.init()
        # Initiating Pygame Mixer
pygame.mixer.init()
        # Declaring track Variable
root.track = StringVar()
        # Declaring Status Variable
root.status = StringVar()

        # Creating the Track Frames for Song label & status label
trackframe = LabelFrame(root, text="Song Track", font=(
            "times new roman", 15, "bold"), bg="Navyblue", fg="white", bd=5, relief=SUNKEN)
trackframe.place(x=0, y=0, width=600, height=100)
        # Inserting Song Track Label
songtrack = Label(trackframe, textvariable=root.track, width=20, font=(
            "times new roman", 24, "bold"), bg="Orange", fg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Inserting Status Label
trackstatus = Label(trackframe, textvariable=root.status, font=(
            "times new roman", 24, "bold"), bg="orange", fg="gold").grid(row=0, column=1, padx=10, pady=5)

        # Creating Button Frame
buttonframe = LabelFrame(root, text="Control Panel", font=(
            "times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=SUNKEN)
buttonframe.place(x=0, y=100, width=600, height=100)
        # Inserting Play Button
playbtn =tkr.Button(buttonframe, text="PLAYSONG", command=playsong, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=0, padx=10, pady=5)
        # Inserting Pause Button
playbtn = tkr.Button(buttonframe, text="PAUSE", command=pausesong, width=8, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=1, padx=10, pady=5)
        # Inserting Unpause Button
playbtn = tkr.Button(buttonframe, text="UNPAUSE", command= unpausesong, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=2, padx=10, pady=5)
        # Inserting Stop Button
playbtn = tkr.Button(buttonframe, text="STOPSONG", command=stopsong, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=3, padx=10, pady=5)

        # Creating Playlist Frame
songsframe = LabelFrame(root, text="Song Playlist", font=(
            "times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=SUNKEN)
songsframe.place(x=600, y=0, width=400, height=200)
        # Inserting scrollbar
scrol_y = Scrollbar(songsframe, orient=VERTICAL)
        # Inserting Playlist listbox
root.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE, font=(
            "times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=SUNKEN)
        # Applying Scrollbar to listbox
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=root.playlist.yview)
root.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
os.chdir("F:\song")
        # Fetching Songs
songtracks = os.listdir()
        # Inserting Songs into Playlist
for track in songtracks:
    root.playlist.insert(END, track)


root.mainloop()
