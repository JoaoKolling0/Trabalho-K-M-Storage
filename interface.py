import tkinter as tk
from tkinter import messagebox
from main import User

class KmstorageApp:
    
    def __init__(self, root):
        self.user = User("Sergão Berranteiro")
        
        root.tittle("K&M Storage")
        
        root.geometry("500x500")
        