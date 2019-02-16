from tkinter import *
from tkinter.ttk import *
import numpy as np


class Doc2VecResultsGUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Classification Results")
        #self.root.geometry('500x500')
        self.root.resizable(False, False)

        # data members
        self.treeview = None
        self.frame = None

        # Operations
        self.init_components()

    def init_components(self):
        self.frame = Frame(master=self.root)
        self.frame.pack(padx=10, pady=10)

        self.treeview = Treeview(master=self.frame)
        self.treeview['columns'] = "percentages"
        self.treeview.heading("#0", text="Topic")
        self.treeview.column("#0", anchor="center")
        self.treeview.heading("percentages", text="Percentage")
        self.treeview.column("percentages", anchor="center")
        self.treeview.pack(fill=X, side=LEFT, expand=1)

        vsb = Scrollbar(master=self.frame, orient="vertical", command=self.treeview.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.treeview.configure(yscrollcommand=vsb.set)

    def display_results(self, topics: list, results: np.array):
        max_percentage = -100.0
        max_topic = ""
        r = results.flatten()

        for i in range(len(topics)):
            self.treeview.insert("", "end", iid=i, text=topics[i], values=(float(r[i]) * 100))

    def d(self, val: str, v: float):
        self.treeview.insert("", "end", iid=1, text=val, values=v)

    def display(self):
        self.root.mainloop()
