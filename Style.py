

main_style = {
    "bg_label" : '#404040',
    "fg_label" : '#00ff00',
    "font" : 'Roboto 15 bold',
    "bg_button" : '#333333',
    "fg_button" : '#66cc00',
    "bg_entry" : '#737373',
    "fg_entry" : '#00ff00'
}


window_style = {
    "title" : 'Auto Clicker',
    "size_h" : 800,
    "size_w" : 600,
    "bg" : '#404040',
    "bd" : 15,
    "relief" : 'ridge',
}


header_label_style = {
    "bg" : '#333333',
    "font" : 'Roboto 25 bold ',
    "fg" : '#00ff00',
    "side" : 'top',
    "padx" : 0,
    "pady" : 20,
    "ipadx" : 100,
}


info_button_style = {
    "bg" : main_style['bg_button'],
    "fg" : main_style['fg_button'],
    "font" : main_style['font'],
    "bd" : 5,
    "relief" : 'ridge',
    "side": 'top',
    "padx": 10,
    "pady": 0,
    "ipadx" : 10,
    "ipady" : 2,
    "anchor" : 'ne',
}


click_times_label_style = {
    "bg" : main_style['bg_label'],
    "fg" : main_style['fg_label'],
    "font" : main_style['font'],
    "padx" : 0,
    "pady" : 2,
    "anchor" : 'center'
}


click_times_entry_style = {
    "bg" : main_style['bg_entry'],
    "fg" : main_style['fg_entry'],
    "font" : main_style['font'],
    "padx" : 0,
    "pady" : 10,
    "anchor" : 'center'
}


click_delay_label_style = {
    "bg" : main_style['bg_label'],
    "fg" : main_style['fg_label'],
    "font" : main_style['font'],
    "padx" : 0,
    "pady" : 2,
    "anchor" : 'center'
}


click_delay_entry_style = {
    "bg" : main_style['bg_entry'],
    "fg" : main_style['fg_entry'],
    "font" : main_style['font'],
    "bbg" : '#333333',
    "padx" : 0,
    "pady" : 10,
    "anchor" : 'center'
}


click_timer_label_style = {
    "bg" : main_style['bg_label'],
    "fg" : main_style['fg_label'],
    "font" : main_style['font'],
    "padx" : 0,
    "pady" : 2,
    "anchor" : 'center'
}


click_timer_entry_style = {
    "bg" : main_style['bg_entry'],
    "fg" : main_style['fg_entry'],
    "font" : main_style['font'],
    "bbg" : '#333333',
    "padx" : 0,
    "pady" : 10,
    "anchor" : 'center'
}


click_button_entry_left_style = {
    "bg" : main_style['bg_button'],
    "fg" : main_style['fg_button'],
    "font" : main_style['font'],
    "padx" : 0,
    "pady" : 2,
    "anchor" : 'center'
}


click_button_entry_right_style = {
    "bg" : main_style['bg_button'],
    "fg" : main_style['fg_button'],
    "font" : main_style['font'],
    "padx" : 0,
    "pady" : 2,
    "anchor" : 'center'
}


button_start_style = {
    "bg" : main_style['bg_button'],
    "fg" : main_style['fg_button'],
    "font" : main_style['font'],
    "bd" : 5,
    "relief" : 'ridge',
    "side" : 'left',
    "padx" : 30,
    "pady" : 25,
    "ipadx" : 25,
    "ipady" : 5,
    "anchor" : 'sw'
}

button_quit_style = {
    "bg" : main_style['bg_button'],
    "fg" : main_style['fg_button'],
    "font" : main_style['font'],
    "bd" : 5,
    "relief" : 'ridge',
    "side" : 'right',
    "padx" : 30,
    "pady" : 25,
    "ipadx" : 25,
    "ipady" : 5,
    "anchor" : 'sw'
}


warning_label_style = {
    "bg" : '#333333',
    "fg" : '#00ff00',
    "font" : 'Roboto 10 bold ',
    "side": 'bottom',
    "padx": 0,
    "pady": 10,
    "ipadx" : 30,
    "ipady" : 20,
    "anchor": 's',
}


temp_info_label_style = {
    "text" : "Clicks -> The number of times the program to click\n"
             "Delay -> in ms, for example, 100 ms for 10 clicks in 1 sec\n"
             "Timer -> Time before the program to start in sec\n"
             "Click start and after the timer, the program will start clicking\n"
             "in the position your mouse is.\n"
             "After all clicks the program will stop clicking.\n",
    "bg" : '#595959',
    "fg" : main_style['fg_button'],
    "font" : 'Roboto 12 bold '
}


temp_info_root_style = {
    "bg" : '#666666',

}


temp_info_button_style = {
    "bg" : main_style['bg_button'],
    "fg" : main_style['fg_button'],
    "font" : 'Roboto 10 bold ',
}


exception_label_style = {
    "text" : "ERROR:\n Empty fields or Not numbers",
    "bg" : '#595959',
    "fg" : main_style['fg_button'],
    "font" : 'Roboto 13 bold '
}


exception_button_style = {
    "bg" : main_style['bg_button'],
    "fg" : main_style['fg_button'],
    "font" : 'Roboto 15 bold ',
}



