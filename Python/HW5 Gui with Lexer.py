from tkinter import *
import re

root = Tk()
root.title("Lexical Analyzer for TinyPie")

Line = 0
firstVar = 1.0
secondVar = 2.0
    
def quit():
    root.destroy()

def cutOneLineTokens(line):
  newLine=[]
  while 1:
    line=line.strip()
    if len(line)==0:
        break
    
    x=re.match(r"(=|\+|>|\*)",line)
    if x is not None:
        newLine.append(f'<operator, {x.group()}>')
        line=line[:x.span()[0]]+line[x.span()[1]:]
        
    x=re.match("(if|int|else|float)",line)
    if x is not None:
        newLine.append(f'<keyword, {x.group()}>')
        line=line[:x.span()[0]]+line[x.span()[1]:]
        
    x=re.match(r"(\(|\)|:|\"|;)",line)
    if x is not None:
        newLine.append(f'<seperator, {x.group()}>')
        line=line[:x.span()[0]]+line[x.span()[1]:]
        
    x=re.match(r"\d+\.\d+",line)
    if x is not None:
        newLine.append(f'<float, {x.group()}>')
        line=line[:x.span()[0]]+line[x.span()[1]:]
        
    x=re.match(r"\d+",line)
    if x is not None:
        newLine.append(f'<literal, {x.group()}>')
        line=line[:x.span()[0]]+line[x.span()[1]:]
        
    x=re.match(r"\w([a-zA-z0-9])*",line)
    if x is not None:
        newLine.append(f'<identifier, {x.group()}>')
        line=line[:x.span()[0]]+line[x.span()[1]:]

  return newLine                     
  newLine=newLine[:-1]

      
def next():
    global Line
    global firstVar
    global secondVar
    name1= cutOneLineTokens(my_text.get(firstVar, secondVar))
    rlen = len(name1)
    for x in range(rlen):
        my_text2.insert(INSERT, name1[x])
        my_text2.insert(INSERT, "\n")
        my_text2.insert(INSERT, "\n")
    firstVar += 1
    secondVar += 1
    Line += 1
    lineLabel = Label(root, text='Current Processing Line: ' + str(Line))
    lineLabel.grid(row=4, column=0)
    
my_text = Text(root, width=20, height=10)
my_text.grid(row=1, column=0)

lineLabel = Label(root, text='Current Processing Line: ' + str(Line))
lineLabel.grid(row=4, column=0)

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
