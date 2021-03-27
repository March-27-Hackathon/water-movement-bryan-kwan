import PySimpleGUI as sg

layout = [  [sg.Text("What do you want to send?")],
            [sg.Input(key='-IN-')],
            [(sg.Button('Send')), (sg.Text("                                                       ")),(sg.Button("Quit"))], 
            [sg.Text("What you write will appear here", key='-Output-')]]

window = sg.Window('Chat', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Quit":
        break
    
    if event == "Send":
        window['-Output-'].update(values['-IN-'])

window.close()