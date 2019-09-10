
#===============================================Imports==============================================================
from pyautogui import *
from Style import *
import time
from tkinter import *


#===================================The functionality of the program=================================================
class ClickEvent:
    def exception_checker(self, clicks, delay, timer, button):
        try:
            int(clicks); int(delay); int(timer)
        except ValueError:
            ExceptionWindow()
        else:
            self.clicks = int(clicks)
            self.delay = int(delay) / 1000
            self.timer = int(timer)
            self.button = button
            self.start_event()

    def start_event(self):
        time.sleep(self.timer)
        click(clicks=self.clicks, interval=self.delay, button=self.button)








#===============================================The Main Window======================================================
class Window(Frame, ClickEvent):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.mouse_button = StringVar(None, 'left')
        self.window_size = 1
        #Check the screen resolution and decide how much to multiply it
        #To make bigger for bigger screens
        if self.winfo_screenheight() > 1000:
            self.window_size = 1.5
        self.widgets()
        self.configurations()
        self.packing()


    #==============================================WIdgets===========================================================
    def widgets(self):

        #===========================================Header===========================================================
        self.header_label = Label(self)

        #=========================================Info Button========================================================
        self.info_button = Button(self)

        #======================================Click Label/Entry=====================================================
        self.click_times_label = Label(self)
        self.click_times_entry = Entry(self)
        self.click_delay_label = Label(self)
        self.click_delay_entry = Spinbox(self)
        self.click_timer_label = Label(self)
        self.click_timer_entry = Spinbox(self)
        self.click_button_entry_left = Radiobutton(self)
        self.click_button_entry_right = Radiobutton(self)
        self.button_start = Button(self)
        self.button_quit = Button(self)
        self.warning_label = Label(self)

    #============================================CONFIGURATIONS======================================================
    def configurations(self):

        #=======================================Window===============================================================
        self.master.title(window_style['title'])
        self.master.geometry(f"{int(window_style['size_h']*self.window_size)}x"
                             f"{int(window_style['size_w']*self.window_size)}")
        self.config(bg=window_style['bg'],
                    bd=window_style['bd'],
                    relief=window_style['relief'],
                    )
        self.pack(fill=BOTH, expand=1)

        #========================================Header==============================================================
        self.header_label.config(text="Auto Clicker",
                                 bg=header_label_style['bg'],
                                 font=header_label_style['font'],
                                 fg=header_label_style['fg'])

        #=======================================Info Button==========================================================
        self.info_button.config(text="Help ?",
                                command=self.information_window,
                                bg=info_button_style['bg'],
                                fg=info_button_style['fg'],
                                font=info_button_style['font'],
                                bd=info_button_style['bd'],
                                relief=info_button_style['relief'])

        #======================================Click Times Label=====================================================
        self.click_times_label.config(text='Clicks',
                                      bg=click_times_label_style['bg'],
                                      fg=click_times_label_style['fg'],
                                      font=click_times_label_style['font'])

        #=====================================Click Times Entry======================================================
        self.click_times_entry.config(bg=click_times_entry_style['bg'],
                                      fg=click_times_entry_style['fg'],
                                      font=click_times_entry_style['font'])

        #=======================================Click Delay Label====================================================
        self.click_delay_label.config(text="Delay",
                                      bg=click_delay_label_style['bg'],
                                      fg=click_delay_label_style['fg'],
                                      font=click_delay_label_style['font'])

        #=======================================Click Delay Entry====================================================
        self.click_delay_entry.config(values=(100, 200, 300,400, 500, 1000),
                                      bg=click_delay_entry_style['bg'],
                                      fg=click_delay_entry_style['fg'],
                                      font=click_delay_entry_style['font'],
                                      buttonbackground=click_delay_entry_style['bbg'])

        #=======================================Click Timer Label====================================================
        self.click_timer_label.config(text="Timer",
                                      bg=click_timer_label_style['bg'],
                                      fg=click_timer_label_style['fg'],
                                      font=click_timer_label_style['font'])

        #=======================================Click Timer Entry====================================================
        self.click_timer_entry.config(values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                                      bg=click_timer_entry_style['bg'],
                                      fg=click_timer_entry_style['fg'],
                                      font=click_timer_entry_style['font'],
                                      buttonbackground=click_timer_entry_style['bbg'])

        #=======================================Click Button Entry===================================================
        self.click_button_entry_left.config(text="Left",
                                            value='left',
                                            indicatoron=0,
                                            width=10,
                                            variable=self.mouse_button,
                                            bg=click_button_entry_left_style['bg'],
                                            fg=click_button_entry_left_style['fg'],
                                            font=click_button_entry_right_style['font'])
        self.click_button_entry_right.config(text="Right",
                                             value='right',
                                             indicatoron=0,
                                             width=10,
                                             variable=self.mouse_button,
                                             bg=click_button_entry_right_style['bg'],
                                             fg=click_button_entry_right_style['fg'],
                                             font=click_button_entry_right_style['font'])

        #======================================Button Start==========================================================
        self.button_start.config(text="Start",
                                 command=self.start_click,
                                 bg=button_start_style['bg'],
                                 fg=button_start_style['fg'],
                                 font=button_start_style['font'],
                                 bd=button_start_style['bd'],
                                 relief=button_start_style['relief'])

        #=======================================Button Quit==========================================================
        self.button_quit.config(text="Quit",
                                 command=lambda: exit(),
                                 bg=button_quit_style['bg'],
                                 fg=button_quit_style['fg'],
                                 font=button_quit_style['font'],
                                 bd=button_quit_style['bd'],
                                 relief=button_quit_style['relief'])

        #========================================Warning Label=======================================================
        self.warning_label.config(text="WARNING!\nTo force stop, go with your mouse\n"
                                       "to the TOP LEFT corner (0x0px)",
                                  bg=warning_label_style['bg'],
                                  fg=warning_label_style['fg'],
                                  font=warning_label_style['font'])


    #==========================================Packing===============================================================
    def packing(self):


        self.header_label.pack(side=header_label_style['side'],
                               padx=header_label_style['padx']*self.window_size,
                               pady=header_label_style['pady']*self.window_size,
                               ipadx=header_label_style['ipadx'])


        self.info_button.pack(side=info_button_style['side'],
                              padx=info_button_style['padx']*self.window_size,
                              pady=info_button_style['pady']*self.window_size,
                              anchor=info_button_style['anchor'],
                              ipadx=info_button_style['ipadx'],
                              ipady=info_button_style['ipady'])


        self.click_times_label.pack(padx=click_times_label_style['padx']*self.window_size,
                                    pady=click_times_label_style['pady']*self.window_size,
                                    anchor=click_times_label_style['anchor'])


        self.click_times_entry.pack(padx=click_times_entry_style['padx']*self.window_size,
                               pady=click_times_entry_style['pady']*self.window_size,
                               anchor=click_times_entry_style['anchor'])


        self.click_delay_label.pack(padx=click_delay_label_style['padx']*self.window_size,
                               pady=click_delay_label_style['pady']*self.window_size,
                               anchor=click_delay_label_style['anchor'])


        self.click_delay_entry.pack(padx=click_delay_entry_style['padx']*self.window_size,
                               pady=click_delay_entry_style['pady']*self.window_size,
                               anchor=click_delay_entry_style['anchor'],)


        self.click_timer_label.pack(padx=click_timer_label_style['padx']*self.window_size,
                               pady=click_timer_label_style['pady']*self.window_size,
                               anchor=click_timer_label_style['anchor'])


        self.click_timer_entry.pack(padx=click_timer_entry_style['padx']*self.window_size,
                               pady=click_timer_entry_style['pady']*self.window_size,
                               anchor=click_timer_entry_style['anchor'])


        self.click_button_entry_left.pack(padx=click_button_entry_left_style['padx']*self.window_size,
                               pady=click_button_entry_left_style['pady']*self.window_size,
                               anchor=click_button_entry_left_style['anchor'])


        self.click_button_entry_right.pack(padx=click_button_entry_right_style['padx']*self.window_size,
                               pady=click_button_entry_right_style['pady']*self.window_size,
                               anchor=click_button_entry_right_style['anchor'])


        self.button_start.pack(side=button_start_style['side'],
                          padx=button_start_style['padx']*self.window_size,
                          pady=button_start_style['pady']*self.window_size,
                          ipadx=button_start_style['ipadx'],
                          ipady=button_start_style['ipady'],
                          anchor=button_start_style['anchor'])


        self.button_quit.pack(side=button_quit_style['side'],
                         padx=button_quit_style['padx']*self.window_size,
                         pady=button_quit_style['pady']*self.window_size,
                         ipadx=button_start_style['ipadx'],
                         ipady=button_start_style['ipady'],
                         anchor=button_quit_style['anchor'])


        self.warning_label.pack(side=warning_label_style['side'],
                           padx=warning_label_style['padx']*self.window_size,
                           pady=warning_label_style['pady']*self.window_size,
                           ipadx=warning_label_style['ipadx'],
                           ipady=warning_label_style['ipady'],
                           anchor=warning_label_style['anchor'])




    def information_window(self):
        temp_info_root = Tk()
        temp_info_root.title("How to use ?")
        temp_info_root.geometry(f"600x400+"
                           f"{int(temp_info_root.winfo_screenwidth()/2)-300}+"
                           f"{int(temp_info_root.winfo_screenheight()/2)-200}")
        temp_info_root.config(bg=temp_info_root_style['bg'])
        temp_info_label = Label(temp_info_root,
                           text=temp_info_label_style['text'],
                           bg=temp_info_label_style['bg'],
                           fg=temp_info_label_style['fg'],
                           font=temp_info_label_style['font'],
                           justify='left')
        temp_info_label.pack(anchor='s',
                             pady=50)
        temp_info_button = Button(temp_info_root,
                            text="I Got It!",
                            command=temp_info_root.destroy,
                            bg=temp_info_button_style['bg'],
                            fg=temp_info_button_style['fg'],
                            font=temp_info_button_style['font'])
        temp_info_button.pack(ipadx=10,
                              ipady=5,
                              pady=20,
                              side='bottom')
        temp_info_root.mainloop()



    def start_click(self):
        test = ClickEvent()
        test.exception_checker(self.click_times_entry.get(),
                          self.click_delay_entry.get(),
                          self.click_timer_entry.get(),
                          self.mouse_button.get())





class ExceptionWindow(Frame):
    def __init__(self):
        self.root = Tk()
        Frame.__init__(self, self.root)
        self.root.title("Error")
        self.root.geometry(f"300x150+"
                           f"{int(self.root.winfo_screenwidth()/2)-150}+"
                           f"{int(self.root.winfo_screenheight()/2)-75}")
        self.root.config(bg='#666666')
        self.label = Label(self.root,
                           text=exception_label_style['text'],
                           bg=exception_label_style['bg'],
                           fg=exception_label_style['fg'],
                           font=exception_label_style['font']).pack(pady=20,
                                                                    )
        self.button = Button(self.root,
                             command=self.root.destroy,
                             text="ok",
                             bg=exception_button_style['bg'],
                             fg=exception_button_style['fg'],
                             font=exception_button_style['font']).pack(side=BOTTOM,
                                                                       padx=10,
                                                                       pady=5,
                                                                       ipadx=10,
                                                                       ipady=0)
        self.root.mainloop()
