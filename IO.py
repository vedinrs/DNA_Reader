import tkinter as tk
from tkinter import *
from tkinter import filedialog
import DNAReader

WIDTH = 400
HEIGHT = 100
BUTTON_WIDTH = 15
BUTTON_HEIGHT = 3

text_file = ""
aa_to_find = ""
root = None
file_select = None
input_box = None
run = None
output_box = None


def initialize():
    root_setup()
    file_select_setup()
    input_box_setup()
    run_setup()
    output_box_setup()

    global root
    root.mainloop()


def root_setup():
    global root
    root = tk.Tk()
    root.title("DNA Reader")
    root.geometry("420x180")


def file_select_setup():
    global file_select
    file_select = Button(text="Select your file",
                             width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                             command=get_file)
    file_select.place(x=0, y=0)


def get_file():
    global text_file
    text_file = filedialog.askopenfilename()
    print(text_file)        # TODO: delete later


def input_box_setup():
    global input_box
    input_box = tk.Text(width=BUTTON_WIDTH, height=BUTTON_HEIGHT / 3)
    input_box.place(x=BUTTON_WIDTH * 10, y=BUTTON_HEIGHT)

def run_setup():
    global run
    run = tk.Button(text="Run",
                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                    command=run_reader)
    run.place(x=BUTTON_WIDTH * 20, y=0)


def run_reader():
    global text_file, aa_to_find, input_box, output_box
    aa_to_find = input_box.get("1.0", "end-1c")
    locations = DNAReader.dna_to_aa_reader(text_file, aa_to_find)
    output_box.config(state=tk.NORMAL)
    output_box.delete(1.0, END)
    if locations:
        output_box.insert(1.0, aa_to_find + " can be found at the following locations: \n" + str(locations))
    else:
        output_box.insert(1.0, aa_to_find + " is not contained within the given sequence")
    output_box.config(state=tk.DISABLED)


def output_box_setup():
    global output_box
    output_box = tk.Text(width=BUTTON_WIDTH*3 + 3, height=BUTTON_HEIGHT*2)
    output_box.place(x=0, y=BUTTON_HEIGHT*20)
    output_box.config(state=tk.DISABLED)
