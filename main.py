from tkinter import *
import pygame
from tkinter.filedialog import askdirectory
import os



root =Tk()



def play():
    pygame.mixer.music.load(play_list.get(ACTIVE))

    var.set(play_list.get(ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


if __name__ == '__main__':
    root.title('Music Player')
    root.geometry('450x350')
    directory = askdirectory()
    os.chdir(directory)  # it permits to change the current directory
    song_list = os.listdir()  # it returns the list of file songs

    play_list = Listbox(root, font='Helvetica 10 bold', bg='yellow', selectmode=SINGLE)
    play_list.pack(fill='both',expand='yes')


    for item in song_list:
        pos = 0
        play_list.insert(pos,item)
        pos = pos + 1

    pygame.init()
    pygame.mixer.init()

    var=StringVar()
    l1=Label(root, font='Helvetica 12 bold',textvariable=var).pack()
    button1=Button(root,width=5,height=3,text='play',command=play,bg='green',relief=SUNKEN,font='Helvetica 10 bold').pack(fill='both',padx=5,pady=5)
    button2=Button(root,width=5,height=3,text='stop',command=stop,bg='red',relief=SUNKEN,font='Helvetica 10 bold').pack(fill='both',padx=5,pady=5)
    button3=Button(root,width=5,height=3,text='pause',command=pause,bg='blue',relief=SUNKEN,font='Helvetica 10 bold').pack(fill='both',padx=5,pady=5)
    button4=Button(root,width=5,height=3,text='unpause',command=unpause,bg='yellow',relief=SUNKEN,font='Helvetica 10 bold').pack(fill='both',padx=5,pady=5)
    root.mainloop()