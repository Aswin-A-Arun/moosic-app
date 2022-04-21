import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path
import time
from ftplib import FTP
from tkinter import filedialog
from pathlib import Path

#import winsound
#Uncomment the beow two line to use pygame to allow mp3 files as well
from playsound import playsound
import pygame
from pygame import mixer

PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox =  None
filePathLabel = None

global song_counter
song_counter = 0





def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)
    
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: " +song_selected)
    else:
       infoLabel.configure(text="")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")


  

   
    

    
        
#Client GUI
def musicWindow(): 
    global song_counter
    global filePathLabel
    global listbox
    global infoLabel
    
    window=Tk()
    window.title('Music Window')
    window.geometry("300x350")
    window.configure(bg='LightSkyBlue')
    
    selectlabel = Label(window, text= "Select Song",bg='LightSkyBlue', font = ("Calibri",8))
    selectlabel.place(x=2, y=1)
    
    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox',bg='LightSkyBlue',borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10,y=18)
    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter = song_counter + 1
        
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)
    
    PlayButton=Button(window,text="Play", width=10,bd=1,bg='SkyBlue',font = ("Calibri",10), command = play)
    PlayButton.place(x=30,y=200)
    
    Stop=Button(window,text="Stop",bd=1,width=10,bg='SkyBlue', font = ("Calibri",10), command = stop)
    Stop.place(x=200,y=200)

       
    
    Upload=Button(window,text="Upload",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10))
    Upload.place(x=30,y=300)
    
    Download =Button(window,text="Download",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10))
    Download.place(x=200,y=300)
    
    infoLabel = Label(window, text= "",fg= "blue",bg='SkyBlue', font = ("Calibri",8))
    infoLabel.place(x=4, y=330)
    
    window.mainloop()
    
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    global song_counter

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

#Initiate Server Connection    
setup()


   




