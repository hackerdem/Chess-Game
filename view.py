import tkinter,copy,sys,configparser
from configuration import *
import controller


class View():
    board_color_1=BOARD_COLOR_1
    board_color_2=BOARD_COLOR_2
    def __init__(self):
        self.controller=controller
        self.parent=parent
        self.create_chess_base()
        self.canvas.bind("<Button-1>",self.on_square_clicked)
    
    def create_chess_base(self):
        self.create_top_menu()
        self.create_canvas()
        self.draw_board()
        self.create_bottom_frame()
        
    def create_top_menu(self):
        self.menu_bar=Menu(self.parent)
        self.create_file_menu()
        self.create_edit_menu()
        self.create_about_menu()
    
    def create_bottom_frame(self):
        self.bottom_frame=Frame(self.parent,height=64)
        self.info_label=Label(self.bottom_frame,text="  White to start the game  ",fg=BOARD_COLOR_2)
        self.info_label.pack(side=RIGHT,padx=8,pady=5)
        self.bottom_frame.pack(fill="x",side="bottom")
    def on_about_menu_clicked(self):
        messagebox.showinfo("chess application for geniouses")
    def on_new_game_menu_clicked(self):
        pass
    def on_preference_menu_clicked(self):pass
    
    def create_file_menu(self):
        self.file_menu=Menu(self.menu_bar,tearoff=0)
        self.file_menu.add_command(label="New Game",command=self.on_new_game_menu_clicked)
        self.menu_bar.add_cascade(label="File",menu=self.file_menu)
        self.parent.config(menu=self.menu_bar)
        
    def create_edit_menu(self):
        self.edit_menu=Menu(self.menu_bar,tearoff=0)
        self.about_menu.add_command(label="About",command=self.on_about_menu_clicked)
        self.menu_bar.add_cascade(label="About",menu=self.about_menu)
        self.parent.config(menu=self.menu_bar)
        
    def create_canvas(self):
        canvas_width=NUMBER_OF_COLUMNS*DIMENSION_OF_EACH_SQUARE
        canvas_height=NUMBER_OF_ROWS*DIMENSION_OF_EACH_SQUARE
        self.canvas=Canvas(self.parent,width=canvas_width,height=canvas_height)
        self.canvas.pack(padx=8,pady=8)
        
    def draw_board(self):
        
    