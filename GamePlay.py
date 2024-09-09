import tkinter as tk
from tkinter import PhotoImage
from tkinter import font as tkFont
import pygame

#Program Points
cs_points = 0
emc_points = 0
is_points = 0

#Game Counter
game_counter = 0

#Game State Update: (Back, Next)
def game_updatePositve():
    global game_counter
    if game_counter < 36:
        game_counter += 1
    check_gameCount()

def game_updateNegative():
    global game_counter
    if game_counter != 0:
        game_counter -= 1
    check_gameCount()

#Check Game State Updates
def convo_time():
    answerCS_button.place_forget()
    answerEMC_button.place_forget()
    answerIS_button.place_forget()
    next_button.place(x=1478, y=750)

def question_time():
    answerCS_button.place(x=730, y=450)
    answerEMC_button.place(x=730, y=550)
    answerIS_button.place(x=730, y=650)
    next_button.place_forget()

#Character Photo Apperance Control
def caleb_photoAppear():
    caleb_image.place(x=460, y=750)
    iris_image.place_forget()
    ezra_image.place_forget()
    cherinne_image.place_forget()

def ezra_photoAppear():
    ezra_image.place(x=460, y=750)
    iris_image.place_forget()
    caleb_image.place_forget()
    cherinne_image.place_forget()

def iris_photoAppear():
    iris_image.place(x=460, y=750)
    caleb_image.place_forget()
    ezra_image.place_forget()
    cherinne_image.place_forget()

def cherinne_photoAppear():
    cherinne_image.place(x=460, y=750)
    iris_image.place_forget()
    ezra_image.place_forget()
    caleb_image.place_forget()

def reader_photoAppear():
    cherinne_image.place_forget()
    iris_image.place_forget()
    ezra_image.place_forget()
    caleb_image.place_forget()

#Game Counter Updates
def check_gameCount():
    global game_counter
    print(game_counter)                                  #For Game "Tick" Monitoring
    caleb_appear = [13,17,21,22,23,24]                   #Game Ticks where Caleb should appear
    ezra_appear = [14,18,25,26,27,28]                    #Game Ticks where Ezra should appear
    iris_appear = [15,19,29,30,31,32,33,34]              #Game Ticks where Iris should appear
    cherinne_appear = [2,3,4,5,7,11,9,12,16,20,35,36]    #Game Ticks where Cherinne should appear

    convo_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
        ,16,17,18,19,21,23,25,27,29,31,33,34,35,36]      #Convo Time Game Ticks
    question_list = [20,22,24,26,28,30,32]               #Question Time Game Ticks

    #Check Game State and Update
    if game_counter in convo_list:
        convo_time()
    elif game_counter in question_list:
        question_time()

    #Check if Game State is on Ending
    if game_counter == 36:                                       #Ending Game Tick
        winning_program = max(cs_points, emc_points, is_points)
        if winning_program == cs_points:                         #CS Ending
            text_label.config(text="You belong in CS!")
        elif winning_program == emc_points:                      #EMC Ending
            text_label.config(text="You belong in EMC!")
        elif winning_program == is_points:                       #IS Ending
            text_label.config(text="You belong in IS!")


    #Check if Game State Requires Character to Appear
    if game_counter in [item - 1 for item in caleb_appear]:
        caleb_photoAppear()
    elif game_counter in [item - 1 for item in ezra_appear]:
        ezra_photoAppear()
    elif game_counter in [item - 1 for item in iris_appear]:
        iris_photoAppear()
    elif game_counter in [item - 1 for item in cherinne_appear]:
        cherinne_photoAppear()
    elif game_counter not in ([item - 1 for item in caleb_appear],[item - 1 for item in ezra_appear],
                              [item - 1 for item in iris_appear],[item - 1 for item in cherinne_appear]):
        reader_photoAppear()


    # Game Object Updates
    answerCS_button.config(text=cs_answers[game_counter])
    answerEMC_button.config(text=emc_answers[game_counter])
    answerIS_button.config(text=is_answers[game_counter])
    text_label.config(text=convo_text[game_counter])

#Action Button Events
def next():
    game_updatePositve()

def quit():
    Gameplay.destroy()

def back():
    game_updateNegative()

def menu():
    pygame.mixer.quit()
    Gameplay.destroy()
    from MainMenu import MainMenu

#Answer Button Events
def ansCS():
    game_updatePositve()
    global cs_points
    cs_points += 1

def ansEMC():
    game_updatePositve()
    global emc_points
    emc_points += 1

def ansIS():
    game_updatePositve()
    global is_points
    is_points += 1

# Game Play Window Creation
Gameplay = tk.Tk()
Gameplay.title("Program Pathfinder")
Gameplay.attributes("-fullscreen", False)

#Background Music
pygame.mixer.init()
pygame.mixer.music.load("Game Data/BGM1.mp3")
pygame.mixer.music.play(loops=99999)
pygame.mixer.music.set_volume(0.25)

#Fonts
actionbutton_font = tkFont.Font(family='Roboto', size=24, weight=tkFont.BOLD)
answerbutton_font = tkFont.Font(family='Roboto', size=12)
textbox_font = tkFont.Font(family='Roboto', size=18)

# IMAGE LOADING
GameBGimgage1 = PhotoImage(file="Game Data/GameBG1.png")
Photolist = [GameBGimgage1]

#Text File Readers
    #Convo
convo_path = "Game Data/Convo"  # Replace with the path to your text file
with open(convo_path, "r") as file:
    convo_text = file.readlines()

    #CS Answers
csanswersfile_path = "Game Data/CS Answers"  # Replace with the path to your text file
with open(csanswersfile_path, "r") as file:
    cs_answers = file.readlines()

    #EMC Answers
emcanswersfile_path = "Game Data/EMC Answers"  # Replace with the path to your text file
with open(emcanswersfile_path, "r") as file:
    emc_answers = file.readlines()

    #IS Answers
isanswersfile_path = "Game Data/IS Answers"  # Replace with the path to your text file
with open(isanswersfile_path, "r") as file:
    is_answers = file.readlines()

# Create a canvas with an image as background
canvas = tk.Canvas(Gameplay, width=1920, height=1080)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=GameBGimgage1)

#Text Box
    #TextBox BG
textbox_image = PhotoImage(file="Game Data/TextBoxBG.png")
textbox_bg = tk.Label(Gameplay, image=textbox_image)
textbox_bg.place(x=460, y=750)
    #textBox Loading
text_label = tk.Label(Gameplay, bg="#2B2020", font=textbox_font, fg="white", text=convo_text[game_counter], wraplength=500, anchor=tk.CENTER,justify=tk.CENTER)
text_label.place(x=860, y=850)

#Character Photos
    #Caleb
caleb_imagepath = PhotoImage(file="Game Data/CalebPic.png")
caleb_image = tk.Label(Gameplay, image=caleb_imagepath)
caleb_image.place(x=460, y=750)

    #Ezra
ezra_imagepath = PhotoImage(file="Game Data/EzraPic.png")
ezra_image = tk.Label(Gameplay, image=ezra_imagepath)
ezra_image.place(x=460, y=750)

    #Iris
iris_imagepath = PhotoImage(file="Game Data/IrisPic.png")
iris_image = tk.Label(Gameplay, image=iris_imagepath)
iris_image.place(x=460, y=750)

    #Cherinne
cherinne_imagepath = PhotoImage(file="Game Data/CherinnePic.png")
cherinne_image = tk.Label(Gameplay, image=cherinne_imagepath)
cherinne_image.place(x=460, y=750)

# Action Buttons
    # Next Button
next_button = tk.Button(canvas, text="Next", font=actionbutton_font, width=5, height=2 ,command = next)
next_button.place(x=1478, y=750)

    # Quit Button
quit_button = tk.Button(canvas, text="Quit", font=actionbutton_font, width=5, height=2 ,command = quit)
canvas.create_window(1530, 915, window=quit_button)

    # Back Button
back_button = tk.Button(canvas, text="Back", font=actionbutton_font, width=5, height=2 ,command = back)
canvas.create_window(395, 802, window=back_button)

    # Menu Button
menu_button = tk.Button(canvas, text="Menu", font=actionbutton_font, width=5, height=2 ,command = menu)
canvas.create_window(395, 915, window=menu_button)
#menu_button.place(x=395, y=915)

# Answer Buttons
    # Next Button
answerCS_button = tk.Button(canvas, text=cs_answers[game_counter], font=answerbutton_font, wraplength=450, width=50, height=3, command=ansCS)
answerCS_button.place(x=730, y=450)

    # Quit Button
answerEMC_button = tk.Button(canvas, text=emc_answers[game_counter], font=answerbutton_font, wraplength=450, width=50, height=3, command=ansEMC)
answerEMC_button.place(x=730, y=550)

    # Back Button
answerIS_button = tk.Button(canvas, text=is_answers[game_counter], font=answerbutton_font, wraplength=450, width=50, height=3, command = ansIS)
answerIS_button.place(x=730, y=650)

#Check Game Count at Initialization
check_gameCount()

#Gameplay Start
Gameplay.mainloop()

