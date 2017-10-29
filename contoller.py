import tkinter,copy,sys,configparser
from configuration import *
import model

class Controller():
    def __init__(self):
        self.init_model()
    def init_model(self):
        self.model=model.Model()