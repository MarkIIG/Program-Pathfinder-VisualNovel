import tkinter as tk
from tkinter import PhotoImage
from tkinter import font as tkFont
import pygame



#button Events
def play():
    pygame.mixer.quit()
    MainMenu.destroy()
    import GamePlay

def quit():
    MainMenu.destroy()

# Main Menu Window Creation
MainMenu = tk.Tk()
MainMenu.title("Program Pathfinder")
MainMenu.attributes("-fullscreen", False)

#BGM
pygame.mixer.init()
pygame.mixer.music.load("Game Data/BGM1.mp3")
pygame.mixer.music.play(loops=99999)
pygame.mixer.music.set_volume(0.25)

#Fonts
button_textfont = tkFont.Font(family='Roboto', size=24, weight=tkFont.BOLD)

# IMAGE LOADING
menu_bgimage = PhotoImage(file="Game Data/MenuBG.png")
Photolist = [menu_bgimage]

# Create a canvas with an image as background
canvas = tk.Canvas(MainMenu, width=1920, height=1080)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=menu_bgimage)

# Buttons
    # Play Button
play_button = tk.Button(canvas, text="Play", font=button_textfont, width=30, height=3 ,command = play)
canvas.create_window(1350, 490, window=play_button)

    # Quit Button
quit_button = tk.Button(canvas, text="Quit", font=button_textfont, width=30, height=3 ,command = quit)
canvas.create_window(1350, 690, window=quit_button)

# Run the MainMenu Loop
MainMenu.mainloop()