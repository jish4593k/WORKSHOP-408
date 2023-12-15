import pygame
import torch
import torch.nn as nn
import torch.optim as optim
import seaborn as sns
import tkinter as tk
from tkinter import messagebox
from moviepy.audio.fx.volumex import volumex
from moviepy.editor import *
import os

video_path = ""



class SimpleNN(nn.Module):
    def __init__(self, input_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, x):
        return self.fc(x)


def train_neural_network(inputs, targets):
    model.train()
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()


def predict(input_data):
    model.eval()
    with torch.no_grad():
        return model(input_data)





def get_button(text, command, window=None, height=None):
    button = tk.Button(window, text=text, command=command, height=height)
    return button


def get_label(text, window=None):
    label = tk.Label(window, text=text)
    return label


def get_entry(window=None, var=None):
    entry = tk.Entry(window, textvariable=var)
    return entry





def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


class VolumeAdjustmentApp:
    def __init__(self, window):
        self.window = window
        self.video_path = ""
        self.create_gui()

    def create_gui(self):
        self.window.title('Volume Adjustment')
        self.window.geometry('280x240')
        self.window.resizable(False, False)
        self.window.configure(background="lightgray")

        self.add_video_button = get_button("Add a Video", self.get_video_file)
        self.add_video_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky='we', columnspan=2)

        self.video_name_label = get_label("No video selected")
        self.video_name_label.grid(row=1, column=0, sticky='we', columnspan=2, pady=(0, 10))

        self.volume_label = get_label("Volume (0 - 100)")
        self.volume_label.grid(row=4, column=0, sticky="w", padx=10, columnspan=2)

        self.volume_value = tk.StringVar(value='50')
        self.volume_entry = get_entry(var=self.volume_value)
        self.volume_entry.grid(row=5, column=0, sticky="we", padx=13, columnspan=2)

        self.volume_value.trace("w", lambda name, index, mode, sv=self.volume_value: validate_volume(self.volume_entry, sv))

        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.back_button = get_button("Back", self.replace_main_window, height=1)
        self.back_button.grid(row=6, column=0, padx=10, sticky="we", pady=(50, 0))

        self.render_button = get_button("Render", command=self.change_volume, height=1)
        self.render_button.grid(row=6, column=1, padx=10, sticky="we", pady=(50, 0))


    def get_video_file(self):
        filename = select_video_file()
        if filename:
            self.video_path = filename
            video_name = filename.split('/')[-1]
            self.video_name_label.config(text=video_name)
            self.add_video_button.config(text='Change Video')

    

if __name__ == "__main__":
    
    sns.set(style="whitegrid")

   
    input_size = 2  
    output_size = 1  
    model = SimpleNN(input_size, output_size)
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

  
    root = tk.Tk()
    app = VolumeAdjustmentApp(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
