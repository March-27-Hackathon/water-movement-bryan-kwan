import PySimpleGUI as sg 
import vlc 


def playVid():
        sg.theme('DarkBlue')

#reusable command to make a button
        def btn(name):
            return sg.Button(name, size=(6,1), pad=(1,1))

#define window content
        layout = [ [sg.Input(default_text='Video URL or Local Path:', size=(30,1), key='-VIDEO_LOCATION-'), sg.Button('load')],
            [sg.Image('',size=(300, 300), key='-VIDEO_OUTPUT-')],
            [btn('previous'), btn('next'), btn('play'), btn('pause'), btn('stop')],
            [sg.Text("I'm a cool dude!", key='-MESSAGE-')],[sg.Button("Quit")]
        ]

#create window
        window = sg.Window('Video Player', layout, element_justification='center', finalize=True, resizable=True)

        window['-VIDEO_OUTPUT-'].expand(True, True)



#video contents

        instance = vlc.Instance()
        list_player = instance.media_list_player_new()
        media_list = instance.media_list_new([])
        list_player.set_media_list(media_list)
        player = list_player.get_media_player()

        player.set_hwnd(window['-VIDEO_OUTPUT-'].Widget.winfo_id())


#display window
        while True:
            event, values = window.read(timeout=1000)
            #check for quit
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break
            if event == 'play':
                list_player.play()
            if event == 'pause':
                list_player.pause()
            if event == 'stop':
                list_player.stop()
            if event == 'next':
                list_player.next()
                list_player.play()
            if event == 'previous':
                list_player.previous()
                list_player.previous() #need to do twice because first call starts video from time = 0
                list_player.play()
            if event == 'load': 
                if values['-VIDEO_LOCATION-'] and not 'Video URL' in values['-VIDEO_LOCATION-']:
                    media_list.add_media(values['-VIDEO_LOCATION-'])
                    list_player.set_media_list(media_list)
                    window['-VIDEO_LOCATION-'].update('Video URL or Local Path:')

    
    #update time  in video
            if player.is_playing():
                window['-MESSAGE-'].update("{:02d}:{:02d} / {:02d}:{:02d}".format(*divmod(player.get_time()//1000, 60),
                                                                     *divmod(player.get_length()//1000, 60)))
            else:
                window['-MESSAGE-'].update('Load media to start' if media_list.count() == 0 else 'Ready to play media' )

        
        window.close()

