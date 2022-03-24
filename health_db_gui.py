import tkinter as tk
from tkinter import ttk
from click import command

from pyparsing import col


def main_window():

    def cancel_cmd():
        root.destroy()

    
    def ok_cmd():
        print("Here is the data")
        entered_name = name_entry.get()
        print("Name: {}".format(entered_name))
        entered_id = id_entry.get()
        print("ID: {}".format(entered_id))
        entered_blood_letter = blood_letter.get()
        entered_rh_factor = rh_factor.get()
        print("Blood type: {}".format(entered_blood_letter+entered_rh_factor))
        

    root = tk.Tk()
    root.title('Health database')
    #if dont want auto resizing can use root.geometry("700x400") by pixels

    ttk.Label(root, text="Blood Donor Database").grid(column=0, row=0,
                                                      columnspan=2,
                                                      sticky=tk.W)
    ttk.Label(root, text="Closest Donation Center").grid(column=2, row=0)

    ttk.Label(root, text="Name:").grid(column=0, row=1,
                                       sticky='e')
    name_entry = tk.StringVar()
    name_entry.set("Enter a name here")
    ttk.Entry(root, width=30, textvariable=name_entry).grid(column=1, row=1, sticky='w')

    ttk.Label(root, text="ID:").grid(column=0, row=2,
                                     sticky='e')
    id_entry = tk.StringVar()
    ttk.Entry(root, textvariable=id_entry).grid(column=1, row=2, sticky='w')

    blood_letter = tk.StringVar()
    ttk.Radiobutton(root, text="A", variable=blood_letter, value="A")\
        .grid(column=0, row=3, sticky='W')
    ttk.Radiobutton(root, text="B", variable=blood_letter, value="B")\
        .grid(column=0, row=4, sticky='W')
    ttk.Radiobutton(root, text="AB", variable=blood_letter, value="AB")\
        .grid(column=0, row=5, sticky='W')
    ttk.Radiobutton(root, text="O", variable=blood_letter, value="O")\
        .grid(column=0, row=6, sticky='W')
    
    rh_factor = tk.StringVar()
    rh_factor.set('+')
    ttk.Checkbutton(root, text="RH Positive", variable=rh_factor,
                    onvalue='+', offvalue='-').grid(column=1, row=4)


    ttk.Button(root, text="OK", command=ok_cmd).grid(column=1, row=6)
    ttk.Button(root, text="Cancel", command=cancel_cmd).grid(column=2, row=6)
    
    donor_center = tk.StringVar()
    center_dropdown = ttk.Combobox(root, textvariable=donor_center)
    center_dropdown.grid(column=2, row=1)
    center_dropdown["values"] = ("Durham", "Raleigh", "Cary", "Apex")
    center_dropdown.state(["readonly"])




    root.mainloop()


if __name__ == "__main__":
    main_window()