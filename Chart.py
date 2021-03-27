import PySimpleGUI as sg
import messagemanager as mm

manager = mm.MessageManager('http://127.0.0.1:4996/messageboard/')
messageboard = manager.get().text

layout = [  [sg.Text("What do you want to send?")],
            [sg.Input(key='-IN-')],
            [(sg.Button('Send')), (sg.Text("                                                       ")),(sg.Button("Quit"))], 
            [sg.Text(messageboard, key='-Output-')]]

window = sg.Window('Chat', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Quit":
        break
    
    if event == "Send":
        response = manager.put(values['-IN-'])
        messageboard = manager.get().text
        window['-Output-'].update(messageboard)

window.close()