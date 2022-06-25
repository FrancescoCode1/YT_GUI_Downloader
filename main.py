import PySimpleGUI as sg
import os



def downloader():
    music_list = []
    sg.theme("DarkTeal")
    #define the layout
    layout = [
        [sg.Text("Input the Videolink:"), sg.InputText(key="-VIDEOLINK-", do_not_clear=False)],
        [sg.Text("                            "), sg.Submit("Add", key="-ADD-", bind_return_key=True, button_color="red")],
        [sg.Text("Format                 "), sg.Radio("wav", key="-WAV-", group_id="format"), sg.Radio("mp3", key="-MP3-", group_id="format")],
        [sg.Text("                            "),sg.Listbox(values=[music_list], size=(45, 6), key="-LIST-")],
        [sg.Submit("Convert", key="-CONVERT-", button_color="red"), sg.Cancel(button_color="red"), sg.Submit("Clear Last", key="-CLEAR_ALL-", button_color="red")]

    ]
    #create instance of the window
    window = sg.Window("Youtube Download Tool", layout)

    #read events and values from window
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        #only for debug purposes
        print(event, values["-VIDEOLINK-"], values["-WAV-"], values["-MP3-"])
        link = values["-VIDEOLINK-"]
        wav = values["-WAV-"]
        mp3 = values["-MP3-"]

        if event == "-ADD-":
            music_list.append(values["-VIDEOLINK-"])
            window["-LIST-"].update(music_list)

        if event == "-CLEAR_ALL-":
            music_list = music_list[:-1]
            window["-LIST-"].update(music_list)


        if event == "-CONVERT-":
            print(music_list)
            if mp3 == True:
                for i in music_list:
                    os.system(f"yt-dlp.exe -f ba -x --audio-format mp3 {i} -o \"\download\%(title)s.%(ext)s\"") #yt-dlp.exe -f ba -x --audio-format mp3 https://www.youtube.com/watch?v=da9PDzt53WA -o "%(id)s.%(ext)s"

                sg.popup(f"DONE!")

            elif wav == True:
                for i in music_list:
                    os.system(f"yt-dlp.exe -f ba -x --audio-format wav {i} -o \"\download\%(title)s.%(ext)s\" ")
                sg.popup(f"DONE!")


    window.close()
downloader()