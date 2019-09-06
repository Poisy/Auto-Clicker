from tkinter import *
from pyautogui import *
from Style.Grid import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.master.title("Auto Clicker")
        self.master.geometry("1000x600")
        self.header()
        self.information_button()
        self.entryes()
        self.buttons()
        self.warning_label()



    def header(self):
        header = Label(self, text="Auto Clicker")
        header.pack(side=header_style['side'],
                    padx=header_style['padx'],
                    pady=header_style['pady'])



    def information_button(self):
        info_button = Button(self, text="How to use ?", command=self.information_window)
        info_button.pack(side=info_button_style['side'],
                         padx=info_button_style['padx'],
                         pady=info_button_style['pady'],
                         anchor=info_button_style['anchor'])



    def entryes(self):
        click_times_label = Label(self, text="Times to click")
        click_times_label.pack(padx=click_times_label_style['padx'],
                               pady=click_times_label_style['pady'],
                               anchor=click_times_label_style['anchor'],
                               )
        click_times_entry = Entry(self)
        click_times_entry.pack(padx=click_times_entry_style['padx'],
                               pady=click_times_entry_style['pady'],
                               anchor=click_times_entry_style['anchor'])

        click_delay_label = Label(self, text="Click Delay")
        click_delay_label.pack(padx=click_delay_label_style['padx'],
                               pady=click_delay_label_style['pady'],
                               anchor=click_delay_label_style['anchor'])
        click_delay_entry = Entry(self)
        click_delay_entry.pack(padx=click_delay_entry_style['padx'],
                               pady=click_delay_entry_style['pady'],
                               anchor=click_delay_entry_style['anchor'],
                               )


    def buttons(self):
        button_start = Button(self, text="Start")
        button_start.pack(side=button_start_style['side'],
                          padx=button_start_style['padx'],
                          pady=button_start_style['pady'],
                          anchor=button_start_style['anchor'])

        button_quit = Button(self, text="Quit")
        button_quit.pack(side=button_quit_style['side'],
                         padx=button_quit_style['padx'],
                         pady=button_quit_style['pady'],
                         anchor=button_quit_style['anchor'])



    def warning_label(self):
        warning_label = Label(self, text="test")
        warning_label.pack(side=warning_label_style['side'],
                           padx=warning_label_style['padx'],
                           pady=warning_label_style['pady'],
                           anchor=warning_label_style['anchor'])



    def information_window(self):
        temp_root = Tk()
        temp_root.mainloop()