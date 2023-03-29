import tkinter as tk
from tkinter import ttk


def set_up_window():
    def ok_btn_cmd():
        print("Ok clicked")
        patient_name = name_value.get()
        patient_id = ID_value.get()
        patient_bt = blood_letter_val.get()
        print(patient_name)
        print(patient_id)
        print(patient_bt)
        return

    def cancel_btn_cmd():
        print("Cancelled")
        root.destroy()
        return

    root = tk.Tk()
    root.title("Donor Database GUI")
    root.geometry("800x800")
    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0)

    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1)
    name_value = tk.StringVar()
    name_entry = ttk.Entry(root, textvariable=name_value)
    name_entry.grid(column=1, row=1)

    ID_label = ttk.Label(root, text="ID:")
    ID_label.grid(column=0, row=2)
    ID_value = tk.StringVar()
    ID_entry = ttk.Entry(root, textvariable=ID_value)
    ID_entry.grid(column=1, row=2)

    ok_button = ttk.Button(root, text="Ok", command=ok_btn_cmd)
    ok_button.grid(column=1, row=6)

    cancel_button = ttk.Button(root, text="Cancel", command=cancel_btn_cmd)
    cancel_button.grid(column=1, row=7)

    blood_letter_val = tk.StringVar()
    A_check = ttk.Radiobutton(root, text="A",
                              variable=blood_letter_val, value="A")
    A_check.grid(column=0, row=3)

    B_check = ttk.Radiobutton(root, text="B",
                              variable=blood_letter_val, value="B")
    B_check.grid(column=0, row=4)

    AB_check = ttk.Radiobutton(root, text="AB",
                               variable=blood_letter_val, value="AB")
    AB_check.grid(column=0, row=5)

    O_check = ttk.Radiobutton(root, text="O",
                              variable=blood_letter_val, value="O")
    O_check.grid(column=0, row=6)

    root.mainloop()
    return


if __name__ == '__main__':
    set_up_window()
    print("End")
