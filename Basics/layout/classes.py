import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title: str, size: tuple):
        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        # widgets
        self.menu = Menu(self)
        self.main = Main(self)

        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        menu_button1 = ttk.Button(self, text='Button 1')
        menu_button2 = ttk.Button(self, text='Button 2')
        menu_button3 = ttk.Button(self, text='Button 3')

        menu_slider1 = ttk.Scale(self, orient='vertical')
        menu_slider2 = ttk.Scale(self, orient='vertical')

        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text='Check 1')
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text='Check 2')

        entry = ttk.Entry(self)

        # main layout
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        menu_button1.grid(row=0, column=0, sticky='nsew', columnspan=2)
        menu_button2.grid(row=0, column=2, sticky='nsew')
        menu_button3.grid(row=1, column=0, sticky='nsew', columnspan=3)

        menu_slider1.grid(row=2, column=0, sticky='nsew', rowspan=2, pady=20)
        menu_slider2.grid(row=2, column=2, sticky='nsew', rowspan=2, pady=20)

        # toggle layout
        toggle_frame.grid(row=4, column=0, sticky='nsew', columnspan=3)
        menu_toggle1.pack(side='left', expand=True)
        menu_toggle2.pack(side='left', expand=True)

        # entry layout
        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        frame1 = MainFrame(
            self,
            {'text': 'Label 1', 'background': 'red'},
            {'text': 'Button 1'}
        )
        frame2 = MainFrame(
            self,
            {'text': 'Label 1', 'background': 'blue'},
            {'text': 'Button 1'}
        )


class MainFrame(ttk.Frame):
    def __init__(self, parent, label_options: dict, button_options: dict):
        super().__init__(parent)
        self.pack(
            side='left',
            expand=True,
            fill='both',
            padx=20,
            pady=20
        )

        self.create_widgets(label_options, button_options)

    def create_widgets(self, label_options, button_options):
        label = ttk.Label(self, **label_options)
        button = ttk.Button(self, **button_options)

        label.pack(expand=True, fill='both')
        button.pack(expand=True, fill='both', pady=10)


App('Class Based App', (600, 600))
