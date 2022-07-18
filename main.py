import PySimpleGUI as sg
import os

music_list = []

def downloader():
    # contains the music in the list
    global music_list
    sg.theme("black")

    # define the layout
    layout = [
        [sg.Text("Link to Video:        ", background_color="#262626"), sg.InputText(key="-VIDEOLINK-", do_not_clear=False)],
        [sg.Text("                            ", background_color="#262626"), sg.Submit("Add", key="-ADD-", bind_return_key=True, button_color=("white", "red"))],
        [sg.Text("Link to Playlist:     ", background_color="#262626"), sg.InputText(key="-PLAYLIST-", do_not_clear=False)],
        [sg.Text("                            ", background_color="#262626"), sg.Submit("Add playlist", key="-ADDPL-", bind_return_key=True, button_color=("white", "red"))],
        [sg.Text("Format                 ", background_color="#262626"), sg.Radio("wav", key="-WAV-", group_id="format", background_color="#262626"),
         sg.Radio("mp3", key="-MP3-", group_id="format", background_color="#262626"), sg.Radio("mp4", key="-MP4-", group_id="format", background_color="#262626")],
        [sg.Text("                            ", background_color="#262626"), sg.Listbox(values=[music_list], size=(45, 6), key="-LIST-")],
        [sg.Text("Path                     ", background_color="#262626"),  sg.InputText(key="-FILEPATH-", default_text="\\download\\", do_not_clear=True),
         sg.FolderBrowse("Save In", key="-SAVEIN-", target="-FILEPATH-")],
        [sg.Text("                            ", background_color="#262626"), sg.Submit("Convert", key="-CONVERT-", button_color=("white", "red")), sg.Cancel(key="-CANCEL-", button_color=("white", "red")), sg.Submit("Clear Last", key="-CLEAR_ALL-", button_color=("white", "red"))],
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

        pllink = values["-PLAYLIST-"]
        link = values["-VIDEOLINK-"]  # link to the video
        wav = values["-WAV-"]  # radio button selector for wav
        mp3 = values["-MP3-"]  # radio button selector for mp3
        mp4 = values["-MP4-"]  # radio button selector for mp4
        fname = values["-FILEPATH-"]  # string filepath


        # adds the link to the link list array
        # link now gets split if it contains &link. Usually in links from playlists
        match event:
            case "-ADD-":
                split_link = link.split("&list", 1)
                normalized_link = split_link[0]
                music_list.append(normalized_link)  # values["-VIDEOLINK-"]
                window["-LIST-"].update(music_list)

            case "-ADDPL-":
                music_list.append(pllink)  # values["-VIDEOLINK-"]
                window["-LIST-"].update(music_list)

            case "-SAVEIN-":
                window["-FILEPATH-"].update(fname)
            case "-OPDONE-":
                music_list = music_list[:-1]
                window["-LIST-"].update(music_list)
            case "-CLEAR_ALL-":
                music_list = music_list[:-1]
                window["-LIST-"].update(music_list)
            case "-CONVERT-":

                # essentially it passes each object in the list to the yt-dlp.exe
                # perform long operation prevents freezing of the screen
                if mp3:
                    for i in music_list:
                        window.perform_long_operation(lambda:
                                                      converter(i, fname, music_list, format="mp3"), "-OPDONE-")

                elif wav:
                    for i in music_list:
                        window.perform_long_operation(lambda:
                                                      converter(i, fname, music_list, format="wav"), "-OPDONE-")

                elif mp4:
                    for i in music_list:
                        window.perform_long_operation(lambda:
                                                      converter(i, fname, music_list, format="mp4"), "-OPDONE-")

    window.close()


def filelog(filepath):
    print("\033[0;32;40msuccessfully\033[0;0m" + " downloaded "  + "to" + f" {filepath}")


def converter(i, fname, musiclist, format):
    os.system(f"yt-dlp.exe -i -f ba -x --audio-format {format} {i} -o \"{fname}\%(title)s.%(ext)s\"")
    filelog(fname)
    music_list = musiclist[:-1]
    return music_list


downloader()
