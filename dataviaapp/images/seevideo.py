import vlc, easygui

from .models import Files 
from .views import *

def seevideo(id):
    file = Files.objects.get(pk=id)
    media = easygui.fileopenbox(
        msg = None,
        title = None,
        default = '~file.media.url',
        filetypes = ["*"]
    )
    
    player = vlc.MediaPlayer(media)
    #player.set_mrl(file.media.url)
    return player.play()
    #player.play()
    #image = "bigles.gif"
    """while True:
        choice = easygui.buttonbox(title="Video Player",msg="Press Play to start",choices=["Play","Pause","Stop","New"])
        print(choice)
        if choice == "Play":
            player.play()
        if choice == "Pause":
            player.pause()
        elif choice == "Stop":
            player.stop()
        elif choice == "New":
            media = easygui.fileopenbox(title="Choose media to open")
            player = vlc.MediaPlayer(media)
        else:
            break"""