import PySimpleGUI as sg
import os


def downloader():
    music_list = []
    sg.theme("black")

    # define the layout
    layout = [

        [sg.Text("Input the Videolink:", background_color="#262626"), sg.InputText(key="-VIDEOLINK-", do_not_clear=False)],
        [sg.Text("                            ", background_color="#262626"), sg.Submit("Add", key="-ADD-", bind_return_key=True, button_color="red")],
        [sg.Text("Format                 ", background_color="#262626"), sg.Radio("wav", key="-WAV-", group_id="format", background_color="#262626"),
         sg.Radio("mp3", key="-MP3-", group_id="format", background_color="#262626"), sg.Radio("mp4", key="-MP4-", group_id="format", background_color="#262626")],
        [sg.Text("                            ", background_color="#262626"), sg.Listbox(values=[music_list], size=(45, 6), key="-LIST-")],
        [sg.Text("Path                     ", background_color="#262626"),  sg.InputText(key="-FILEPATH-", default_text="\\download\\", do_not_clear=True),
         sg.FolderBrowse("Save In", key="-SAVEIN-", target="-FILEPATH-")],
        [sg.Text("                            ", background_color="#262626"), sg.Submit("Convert", key="-CONVERT-", button_color="red"), sg.Cancel(button_color="red"), sg.Submit("Clear Last", key="-CLEAR_ALL-", button_color="red")],
        [sg.Text("Please make sure yt-dlp and ffmpeg is in PATH or installed in the same directory as this .exe", background_color="#262626")],
        [sg.Text("Please dont use this programm to illegally download music or other copyrighted material, \ni take no responsibility for damages", background_color="#262626")]
    ]

    # create instance of the window
    window = sg.Window("Youtube Download Tool", layout, background_color="#262626")

    # read events and values from window
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        # only for debug purposes
        # print(event, values["-VIDEOLINK-"], values["-WAV-"], values["-MP3-"])

        link = values["-VIDEOLINK-"]
        wav = values["-WAV-"]
        mp3 = values["-MP3-"]
        mp4 = values["-MP4-"]
        fname = values["-FILEPATH-"]

        print(link, wav, mp4, mp3, fname)
        if event == "-ADD-":
            music_list.append(link)  # values["-VIDEOLINK-"]
            window["-LIST-"].update(music_list)

        if event == "-SAVEIN-":
             # values["-VIDEOLINK-"]
            window["-FILEPATH-"].update(fname)

        if event == "-CLEAR_ALL-":
            music_list = music_list[:-1]
            window["-LIST-"].update(music_list)

        if event == "-CONVERT-":
            print(music_list)
            if mp3:
                for i in music_list:
                    os.system(f"yt-dlp.exe -f ba -x --audio-format mp3 {i} -o \"{fname}\%(title)s.%(ext)s\"") # yt-dlp.exe -f ba -x --audio-format mp3 https://www.youtube.com/watch?v=da9PDzt53WA -o "%(id)s.%(ext)s"
                sg.popup(f"DONE!")

            elif wav:
                for i in music_list:
                    os.system(f"yt-dlp.exe -f ba -x --audio-format wav {i} -o \"\{fname}\%(title)s.%(ext)s\" ")
                sg.popup(f"DONE!")

            elif mp4:
                for i in music_list:
                    os.system(f"yt-dlp -f bv*+ba {i} -o \"\{fname}\%(title)s.%(ext)s\" ")
                sg.popup(f"DONE!")

    window.close()


downloader()
