import PySimpleGUI as sg 
import Video

layout = [ [sg.Text("Where would you like to go?", justification='center', size=(100,5), textsize=(15,5))], [sg.Button("Chat room",size=(33,5)), 
        sg.Button("Video Library", size=(34,5)), sg.Button("Workshops", size=(33,5))], [sg.Button("Quit")] ]

window = sg.Window('Water Movement', layout, size=(900,275))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Quit":
        break
    if event == "Chat room":
        sg.popup("This is the Chat room")
        
    if event == 'Video Library':
        Video.playVid()

    if event == "Workshops":
        sg.popup("This is Workshop area")

window.close()

