from tkinter import *
from configuration import *
import model,piece

class Controller():

    def __init__(self):
        self.init_model()

    def init_model(self):
        self.model = model.Model()
        
    def get_all_pieces_on_chess_board(self):
        return self.model.items()
    def reset_game_data(self):
        self.model.reset_game_data()
    def reset_to_initial_locations(self):
        self.model.reset_to_initial_locations()
    def get_numeric_notation(self,position):
        return piece.get_numeric_notation(position)
   
    
    
    