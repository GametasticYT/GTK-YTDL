import gi, os

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class MainWin(Gtk.Window):
    def init_ui(self):
        self.set_default_size(500, 100)
    def __init__(self):
        Gtk.Window.__init__(self, title="Youtube-dl Wrapper")
        
        self.MP3box = Gtk.Box(spacing=6)
        self.add(self.MP3box)
        
        self.btn1 = Gtk.Button(label="MP3")
        self.btn1.connect("clicked", self.MP3DL)
        self.MP3box.pack_start(self.btn1, True, True, 0)

        self.btn2 = Gtk.Button(label="MP4")
        self.btn2.connect("clicked", self.MP4DL)
        self.MP3box.pack_start(self.btn2, True, True, 0)


    def MP3DL(self, widget):
        musicfile = open("music.txt")
        for url in musicfile:
            os.system("youtube-dl -o 'Musik/%(title)s.%(ext)s' -x --audio-format mp3 " + url)
        for x in range(5):
            print("Fertig!")


    def MP4DL(self, widget):
        vidfile = open("videos.txt")
        for url in vidfile:
            os.system("youtube-dl -o 'Videos/%(title)s.%(ext)s' " + url)
        for x in range(5):
            print("Fertig!")


win = MainWin()
win.init_ui()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()