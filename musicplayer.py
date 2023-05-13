from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

music = Tk()
music.title("Music Player")
music.geometry("515x500+260+85")
music.resizable(False,False)
rootpath="E:\SONGS"

mixer.init()

def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)


def play_song():
    musiic_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    m.config(text=musiic_name[0:30])
    
def play_next():
    next_song =playlist.curselection()
    next_song=next_song[0]+1
    next_song_name =playlist.get(next_song)
    m.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    playlist.select_clear(0,'end')
    playlist.activate(next_song)
    playlist.select_set(next_song)
    
def play_prev():
    next_song =playlist.curselection()
    next_song=next_song[0]-1
    next_song_name =playlist.get(next_song)
    m.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    playlist.select_clear(0,'end')
    playlist.activate(next_song)
    playlist.select_set(next_song)

        
images =PhotoImage(file="music.png")
music.iconphoto(False,images)
Top=PhotoImage(file="image.png")
Label(music,image=Top).pack()

logo =PhotoImage(file="music.png")
Label(music,image=images).place(x=150,y=315)


playbutton=PhotoImage(file="play.png")
Button(music,text= "Play",image=playbutton,bg="#0f1a2b",bd=0,command=play_song).place(x=175,y=406)

pause=PhotoImage(file="pause.png")
pb=tk.Button(music,text="Pause",image=pause,bg="#0f1a2b",command=mixer.music.pause).place(x=235,y=410)

resume=PhotoImage(file="resume.png")
Button(music,text="Pause",image=resume,bg="#0f1a2b",command=mixer.music.unpause).place(x=285,y=410)

stop=PhotoImage(file="stop.png")
Button(music,image=stop,bg="#0f1a2b",command=mixer.music.stop).place(x=115,y=410)

m=Label(music,text="",width=40,font=('ds-digital',15),fg="white",bg="#0f1a2b")
m.place(x=222,y=480,anchor="center")

menu=PhotoImage(file="menu1.png")
Label(music,image= menu,bg="#0f1a2b").place(x=10,y=20)

mf=Frame(music,bd=6,relief=RIDGE)
mf.place(x=25,y=30,width=465,height=300)

Button(music,text="OPEN FOLDER",width=15,height=2,font=("arial",10,"bold"),fg="white",bd="5",bg="red",command=open_folder).place(x=355,y=340)

scroll=Scrollbar(mf)
playlist=Listbox(mf,width=61,height=15,font=("arial",10),bg="dark gray",fg="grey",selectbackground="lightblue",
                  cursor="hand2",bd=0,yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)

playlist.place(x=5,y=20)


music.mainloop()


