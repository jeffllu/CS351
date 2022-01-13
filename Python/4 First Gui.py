from tkinter import *

root = Tk()
root.title("Lexical Analyzer for TinyPie")

Line = 0
firstVar = 1.0
secondVar = 2.0
    
def quit():
    root.destroy()

def next():
    global Line
    global firstVar
    global secondVar
    my_text2.insert(END, my_text.get(firstVar, secondVar))
    firstVar += 1
    secondVar += 1
    Line += 1
    lineLabel = Label(root, text='Current Processing Line: ' + str(Line))
    lineLabel.grid(row=4, column=0)

lineLabel = Label(root, text='Current Processing Line: ' + str(Line))
lineLabel.grid(row=4, column=0)
    
my_text = Text(root, width=20, height=10)
my_text.grid(row=1, column=0)


my_text2 = Text(root, width=20, height=10)
my_text2.grid(row=1, column=5)

quit_button = Button(root, text="Quit", command=quit)
quit_button.grid(row=5, column=5)

next_button = Button(root, text="Next Line", command=next)
next_button.grid(row=5, column=0, padx=20)

my_label = Label(root, text='')
my_label.grid(row=3, column=3)
label1 = Label(root, text='Lexical Analyzed Result:')
label1.grid(row=0, column=5)
label2= Label(root, text='Source Code Input:')
label2.grid(row=0, column=0)

root.mainloop()
