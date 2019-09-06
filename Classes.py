from tkinter import *
from pyautogui import *
from Style.Pack import *
import time


class ClickEvent:
    def __init__(self, clicks, delay, timer, button):
        self.clicks = int(clicks)
        self.delay = int(delay) / 1000
        self.timer = int(timer)
        self.button = button

    def start_event(self):
        time.sleep(self.timer)
        click(clicks=self.clicks, interval=self.delay, button=self.button)

class Window(Frame, ClickEvent):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.master.title("Auto Clicker")
        self.master.geometry("1100x700")
        self.mouse_button = StringVar(None, 'left')
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
        self.click_times_label = Label(self, text="Clicks")
        self.click_times_label.pack(padx=click_times_label_style['padx'],
                               pady=click_times_label_style['pady'],
                               anchor=click_times_label_style['anchor'],
                               )
        self.click_times_entry = Entry(self)
        self.click_times_entry.pack(padx=click_times_entry_style['padx'],
                               pady=click_times_entry_style['pady'],
                               anchor=click_times_entry_style['anchor'])

        self.click_delay_label = Label(self, text="Delay")
        self.click_delay_label.pack(padx=click_delay_label_style['padx'],
                               pady=click_delay_label_style['pady'],
                               anchor=click_delay_label_style['anchor'])
        self.click_delay_entry = Spinbox(self, values=(100, 200, 300,
                                                       400, 500, 1000))
        self.click_delay_entry.pack(padx=click_delay_entry_style['padx'],
                               pady=click_delay_entry_style['pady'],
                               anchor=click_delay_entry_style['anchor'],
                               )
        self.click_timer_label = Label(self, text="Timer")
        self.click_timer_label.pack(padx=click_timer_label_style['padx'],
                               pady=click_timer_label_style['pady'],
                               anchor=click_timer_label_style['anchor'])

        self.click_timer_entry = Spinbox(self, values=(1, 2, 3, 4, 5,
                                                  6, 7, 8, 9, 10))
        self.click_timer_entry.pack(padx=click_timer_entry_style['padx'],
                               pady=click_timer_entry_style['pady'],
                               anchor=click_timer_entry_style['anchor'],
                               )

        self.click_button_label = Label(self, text="Button")
        self.click_button_label.pack(padx=click_button_label_style['padx'],
                               pady=click_button_label_style['pady'],
                               anchor=click_button_label_style['anchor'],
                               )

        self.click_button_entry_left = Radiobutton(self, text="Left", value='left',
                                                   indicatoron=0, width=10,
                                                   variable=self.mouse_button)
        self.click_button_entry_right = Radiobutton(self, text="Right", value='right',
                                                    indicatoron=0, width=10,
                                                    variable=self.mouse_button)
        self.click_button_entry_left.pack(padx=click_button_entry_left_style['padx'],
                               pady=click_button_entry_left_style['pady'],
                               anchor=click_button_entry_left_style['anchor'],
                               )
        self.click_button_entry_right.pack(padx=click_button_entry_right_style['padx'],
                               pady=click_button_entry_right_style['pady'],
                               anchor=click_button_entry_right_style['anchor'],
                               )


    def buttons(self):
        button_start = Button(self, text="Start", command=self.start_click)
        button_start.pack(side=button_start_style['side'],
                          padx=button_start_style['padx'],
                          pady=button_start_style['pady'],
                          anchor=button_start_style['anchor'])

        button_quit = Button(self, text="Quit", command=lambda: exit())
        button_quit.pack(side=button_quit_style['side'],
                         padx=button_quit_style['padx'],
                         pady=button_quit_style['pady'],
                         anchor=button_quit_style['anchor'])



    def warning_label(self):
        warning_label = Label(self, text="WARNING!\n"
                                         "To stop press SPACE")
        warning_label.pack(side=warning_label_style['side'],
                           padx=warning_label_style['padx'],
                           pady=warning_label_style['pady'],
                           anchor=warning_label_style['anchor'])




    def information_window(self):
        temp_root = Tk()
        temp_root.title("How to use ?")
        temp_root.geometry("500x400")
        temp_label = Label(temp_root, text="Clicks -> The number of times the program to click\n"
                                           "Delay -> in ms, for example, 100 ms for 10 click in 1 sec\n"
                                           "Timer -> Time before the program to start in sec\n"
                                           "Click start and after the timer, the program will start clicking\n"
                                           "in the position your mouse is.\n"
                                           "After all click the program will stop clicking.\n"
                                           "You can emergency stop the program by pressing 'SPACE'.")
        temp_label.pack()
        temp_root.mainloop()



    def start_click(self):
        test = ClickEvent(self.click_times_entry.get(),
                          self.click_delay_entry.get(),
                          self.click_timer_entry.get(),
                          self.mouse_button.get())
        test.start_event()



