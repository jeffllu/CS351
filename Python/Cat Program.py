from tkinter import *

class Database:
    def __init__(self):
        self.cat_list = []
    def add_cat(self, info):
        self.cat_list.append(info)
    def print_database(self):
        print("*********************************")
        print("My Cat Registration System")
        print("*********************************")
        print("Name, ID")
        for i in self.cat_list:
            print(i[0]+','+'{:0>4}'.format(i[1]))
            
class MyFirstGUI:
    def __init__(self, root):
        self.master = root
        self.master.title("My Cat Registration System")

        self.id = StringVar()
        self.name = StringVar()
        self.database = Database()

        self.label = Label(self.master, text="Cat Name: ")
        self.label.grid(row=0,column=0,sticky=E)

        self.catnameentry = Entry(self.master)
        self.catnameentry.grid(row=0, column=1, sticky=E)

        self.label2 = Label(self.master, text="Cat ID: ")
        self.label2.grid(row=0, column=2, sticky =E)

        self.catnameentry2 = Entry(self.master)
        self.catnameentry2.grid(row=0, column=3, sticky=E)
        
        self.submitbutton = Button (self.master, text="Submit name", command=self.submitname)
        self.submitbutton.grid(row=0,column=4, sticky=E)

        self.label3 = Label(self.master, text="Registered cat name: ")
        self.label3.grid(row=1,column=0,sticky=E)

        self.grayEntry1 = Entry(self.master, text="", textvariable=self.name)
        self.grayEntry1.grid(row=1, column=1, sticky=E)
        self.grayEntry1['state'] = 'disabled'

        self.label4 = Label(self.master, text="Registered ID: ")
        self.label4.grid(row=1, column=2, sticky=E)

        self.grayEntry2 = Entry(self.master, text="", textvariable=self.id)
        self.grayEntry2.grid(row=1, column=3, sticky=E)
        self.grayEntry2['state'] = 'disabled'

        self.printbutton = Button(self.master, text="Print Database", command=self.printdatabase)
        self.printbutton.grid(row=1, column=4, sticky=E)

    def submitname(self):
        if self.catnameentry.get()=="" or self.catnameentry2.get()=="":
            print("Invalid Entry")
        else:
            self.id.set(self.catnameentry2.get())
            self.name.set(self.catnameentry.get())
            self.database.add_cat((self.catnameentry.get(),self.catnameentry2.get()))
            print ("a cat name submitted")
            
    def printdatabase(self):
        self.database.print_database()

if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = MyFirstGUI(myTkRoot)
    myTkRoot.mainloop()

