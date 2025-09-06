# Data_entry_app
"""The ABQ Data Entry application"""

## First step

import tkinter as tk
import tkinter.ttk as ttk
# Generate a datestring for the filename
from datetime import datetime
# Used for some file operations in our save routine
from pathlib import Path
import csv

# Global variables
variables = dict()
records_saved = 0

# Create and configure the root window
root = tk.Tk()
root.title('ABQ Data Entry Application')
root.columnconfigure(0, weight=1)

# heading for the application
ttk.Label(
    root,
    text="ABQ Data Entry Application",
    font = ("TkDefaultFont", 16),
).grid()

## Building the data record form
drf = ttk.Frame(root)
drf.grid(padx=10, sticky=(tk.E, tk.W))
drf.columnconfigure(0, weight=1)

## The Record Information section
r_info = ttk.LabelFrame(drf, text="Record Information")
r_info.grid(sticky=(tk.E, tk.W))
for i in range(3):
    r_info.columnconfigure(i, weight=1)
variables['data'] = tk.StringVar()
ttk.Label(r_info,text = "Data").grid(row = 0, column = 0)
ttk.Entry(
    r_info,
    textvariable = variables['data'],
).grid(row = 1, column = 0, sticky=(tk.E, tk.W))
time_values = ['8:00','12:00', '16:00', '20:00']
variables['time'] = tk.StringVar()
ttk.Label(r_info,text = "Time").grid(row = 0, column = 1)
ttk.Combobox(
    r_info,
    values = time_values,
    textvariable = variables['time'],
).grid(row = 1, column = 1, sticky=(tk.E, tk.W))
variables['technician'] = tk.StringVar()
ttk.Label(r_info, text='Technician').grid(row=0, column=2)
ttk.Entry(
    r_info,
    textvariable=variables['technician']
).grid(row=1, column=2, sticky=(tk.W + tk.E))
variables['lab'] = tk.StringVar()
ttk.Label(r_info, text='Lab').grid(row=2, column=0)
labframe = ttk.Frame(r_info)
for lab in ('A', 'B', 'C'):
    ttk.Radiobutton(
        labframe,
        value=lab,
        text = lab,
        variable = variables['lab'],
    ).pack(side=tk.LEFT,expand=True)
labframe.grid(row=3,column=0,sticky=(tk.E,tk.W))
variables['plot'] = tk.IntVar()
ttk.Label(r_info, text='Plot').grid(row=2, column=1)
ttk.Combobox(
    r_info,
    textvariable=variables['plot'],
    values=list(range(1,21)),
).grid(row=3, column=1, sticky=(tk.E,tk.W))
variables['seed_sample'] = tk.StringVar()
ttk.Label(r_info, text='Seed Sample').grid(row=2, column=2)
ttk.Entry(
    r_info,
    textvariable=variables['seed_sample'],
).grid(row=3, column=2, sticky=(tk.E,tk.W))

## Environment Data section
e_info = ttk.LabelFrame(drf, text="Environment Data")
e_info.grid(sticky=(tk.E, tk.W))
for i in range(3):
    e_info.columnconfigure(i, weight=1)
variables['humidity'] = tk.DoubleVar()
ttk.Label(e_info, text= "Humidity(g/m^3)").grid(row = 0, column = 0)
ttk.Spinbox(
    e_info,
    textvariable = variables['humidity'],
    from_ = 0.5, to = 52.0,
    increment = 0.1,
).grid(row = 1, column = 0, sticky=(tk.E, tk.W))
variables['light'] = tk.DoubleVar()
ttk.Label(e_info, text="Light(Klx)").grid(row = 0, column = 1)
ttk.Spinbox(
    e_info,
    textvariable = variables['light'],
    from_ = 0, to = 100, increment = 0.1,
).grid(row = 1, column = 1, sticky=(tk.E, tk.W))
variables['temperature'] = tk.DoubleVar()
ttk.Label(e_info, text="Temperature(C)").grid(row = 0, column = 2)
ttk.Spinbox(
    e_info,
    textvariable = variables['temperature'],
    from_ = 4, to = 40,
    increment = 0.1,
).grid(row = 1, column = 2, sticky=(tk.E, tk.W))
variables['equipment_fault'] = tk.BooleanVar()
ttk.Checkbutton(
    e_info,
    variable = variables['equipment_fault'],
    text = "Equipment Fault",
).grid(row =2, column = 0, sticky=tk.W, pady=5)

## Plant Data section
p_info = ttk.LabelFrame(drf,text="Plant data")
p_info.grid(sticky=(tk.E, tk.W))
for i in range(3):
    p_info.columnconfigure(i, weight=1)

variables['plant'] = tk.IntVar()
ttk.Label(p_info, text="Plant").grid(row = 0, column = 0)
ttk.Spinbox(
    p_info,
    textvariable = variables['plant'],
    from_ = 0, to = 20,
    increment = 1
).grid(row = 1, column = 0, sticky=(tk.E, tk.W))
variables['blossoms'] = tk.IntVar()
ttk.Label(p_info,text="Blossoms").grid(row = 0, column = 1)
ttk.Spinbox(
    p_info,
    textvariable = variables['blossoms'],
    from_ = 0, to = 1000,
    increment = 1
).grid(row = 1, column = 1, sticky=(tk.E, tk.W))
variables['fruit'] = tk.IntVar()
ttk.Label(p_info, text="Fruit").grid(row = 0, column = 2)
ttk.Spinbox(
    p_info,
    textvariable = variables['fruit'],
    from_ = 0, to = 1000,
    increment = 1
).grid(row = 1, column = 2, sticky=(tk.E, tk.W))
variables['min_height'] = tk.DoubleVar()
ttk.Label(p_info, text="Minimum Height(cm)").grid(row = 2, column = 0)
ttk.Spinbox(
    p_info,
    textvariable= variables['min_height'],
    from_ = 0, to = 1000,
    increment = .1
).grid(row=3,column = 0, sticky=(tk.E, tk.W))
variables['max_height'] = tk.DoubleVar()
ttk.Label(p_info, text="Maximum Height(cm)").grid(row = 2, column = 1)
ttk.Spinbox(
    p_info,
    textvariable= variables['max_height'],
    from_ = 0, to = 1000,
    increment = .1
).grid(row=3,column = 1, sticky=(tk.E, tk.W))
variables['mid_height'] = tk.DoubleVar()
ttk.Label(p_info,text="Mid Height(cm)").grid(row = 2, column = 2)
ttk.Spinbox(
    p_info,
    textvariable= variables['mid_height'],
    from_ = 0, to = 1000,
    increment=.1
).grid(row=3,column = 2, sticky=(tk.E, tk.W))

## Finishing the GUI
ttk.Label(drf,text="Notes").grid()
notes_inp = tk.Text(drf,width=75,height=10)
notes_inp.grid(sticky=(tk.E,tk.W))
buttons = tk.Frame(drf)
buttons.grid(sticky=(tk.E,tk.W))
save_button = ttk.Button(buttons,text = "Save")
save_button.pack(side=tk.RIGHT)
reset_button = ttk.Button(buttons,text = "Reset")
reset_button.pack(side=tk.RIGHT)

# Status bar
status_variable = tk.StringVar()
ttk.Label(root,textvariable=status_variable).grid(sticky=(tk.E,tk.W),row=99,padx = 10)

## Writing the callback functions
def on_reset():
    """Called when reset button is clicked, or after save"""
    for variable in variables.values():
        #print(variable)
        if isinstance(variable, tk.BooleanVar):
            variable.set(False)
        else:
            variable.set('')
    notes_inp.delete(1.0, tk.END)
reset_button.configure(command=on_reset)

## Save callback
def on_save():
    """Handle save button clicks"""
    global records_saved
    datestring = datetime.today().strftime("%Y-%m-%d")
    filename = f"abq_data_record_{datestring}.csv"
    newfile = not Path(filename).exists()
    data = dict()
    fault = variables['equipment_fault'].get()
    for key, variable in variables.items():
        if fault and key in ('light','humidity','temperature'):
            data[key] = ''
        else:
            try:
                data[key] = variable.get()
            except tk.TclError:
                status_variable.set(f"Error in field: {key}. Data not saved,")
                return
    # get the Text widget contents separately
    data['notes'] = notes_inp.get(1.0, tk.END)

    with open(filename,'a',newline='') as fh:
        csv_writer = csv.DictWriter(fh, fieldnames=data.keys())
        if newfile:
            csv_writer.writeheader()
        csv_writer.writerow(data)

    records_saved += 1
    status_variable.set(f"{records_saved} records saved this session")
    on_reset()

save_button.configure(command=on_save)
on_reset()






root.mainloop()








