import tkinter as tk
from tkinter import *
from tkinter import filedialog
import DNAReader

WIDTH = 400
HEIGHT = 150
BUTTON_WIDTH = 15
BUTTON_HEIGHT = 3

text_file = ""
root = None
file_select = None
input_box = None
run = None
output_box = None


def initialize():
    global root, input_box, output_box
    root_setup()
    file_select_setup()
    input_box_setup()
    output_box_setup()
    run_setup(input_box, output_box)

    root.mainloop()


def root_setup():
    global root
    root = tk.Tk()
    root.title("DNA Reader")
    #root.geometry(str(WIDTH) + "x" + str(HEIGHT))


def file_select_setup():
    global file_select, root
    file_select = Button(text="Select your file",
                         width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                         command=get_file)
    file_select.grid(column=0, row=0)


def get_file():
    global text_file
    text_file = filedialog.askopenfilename()


def input_box_setup():
    global input_box
    input_box = tk.Text(width=int(BUTTON_WIDTH*1.5), height=BUTTON_HEIGHT / 3)
    input_box.grid(column=1, row=0, padx=10)


def run_setup(input_box, output_box):
    global run
    run = tk.Button(text="Run",
                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                    command=lambda entry=input_box, output=output_box: run_reader(entry, output))
    run.grid(column=2, row=0)


def run_reader(entry, output):
    global text_file
    aa_to_find = entry.get(1.0, "end-1c")
    try:
        locations = DNAReader.dna_to_aa_reader(text_file, aa_to_find)
    except FileNotFoundError:
        output.config(state=tk.NORMAL)
        output.delete(1.0, END)
        output.insert(1.0, "Error: No File Selected")
        output.config(state=tk.DISABLED)
        return
    except DNAReader.NoAAEntryException:
        output.config(state=tk.NORMAL)
        output.delete(1.0, END)
        output.insert(1.0, "Error: No Amino Acid Sequence Given")
        output.config(state=tk.DISABLED)
        return
    output.config(state=tk.NORMAL)
    output.delete(1.0, END)
    if locations:
        output.insert(1.0, aa_to_find + " can be found at the following locations: \n" + str(locations))
    else:
        output.insert(1.0, aa_to_find + " is not contained within the given sequence")
    output.config(state=tk.DISABLED)


def output_box_setup():
    global output_box
    output_box = tk.Text(width=BUTTON_WIDTH*3, height=BUTTON_HEIGHT*2)

    output_box.config(state=tk.DISABLED)
    output_box.grid(column=0, row=1, pady=(10, 0), columnspan=3, sticky=tk.W+tk.E)
