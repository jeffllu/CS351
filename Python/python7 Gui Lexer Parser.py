from tkinter import *
import re

root = Tk()
root.title("Lexical Analyzer for TinyPie")

Line = 0
firstVar = 1.0
secondVar = 2.0
newLine=[]
inToken = ("empty","empty")

def quit():
    root.destroy()

def cutOneLineTokens(line):
  global newLine
  newLine=[]
  while 1:
    line=line.strip()
    if len(line)==0:
        break
    
    x=re.match(r"(=|\+|>|\*)",line)
    if x is not None:
        newLine.append("<" + "operator," + x.group() +">")
        line=line[:x.span()[0]]+line[x.span()[1]:]
        
    x=re.match("(if|int|else|float)",line)
    if x is not None:
        newLine.append("<" + "keyword," + x.group() + ">")
        line=line[:x.span()[0]]+line[x.span()[1]:]
        
    x=re.match(r"(\(|\)|:|\"|;)",line)
    if x is not None:
        newLine.append("<" + "seperator," + x.group() + ">")
        line=line[:x.span()[0]]+line[x.span()[1]:]
        
    x=re.match(r"\d+\.\d+",line)
    if x is not None:
        newLine.append("<" +"float," + x.group() + ">")
        line=line[:x.span()[0]]+line[x.span()[1]:]
        
    x=re.match(r"\d+",line)
    if x is not None:
        newLine.append("<" + "int," + x.group() + ">")
        line=line[:x.span()[0]]+line[x.span()[1]:]
        
    x=re.match(r"\w([a-zA-z0-9])*",line)
    if x is not None:
        newLine.append("<" + "identifier," + x.group() +">")
        line=line[:x.span()[0]]+line[x.span()[1]:]
        
  print(newLine)
  return newLine                     
  newLine=newLine[:-1]

def next():
    global newLine
    global Line
    global firstVar
    global secondVar
    name1= cutOneLineTokens(my_text.get(firstVar, secondVar))
    rlen = len(name1)
    for x in range(rlen):
        my_text2.insert(INSERT, name1[x])
        my_text2.insert(INSERT, "\n")
        my_text2.insert(INSERT, "\n")
    global newToken
    newToken = [tuple(y.strip("<>").replace('"', '').split(",")) for y in newLine]
    my_text3.insert(INSERT, "###Parse tree for line " + str(Line+1) + '###\n')
    parser(newToken)
    firstVar += 1
    secondVar += 1
    Line += 1
    lineLabel = Label(root, text='\nCurrent Processing Line: ' + str(Line) + '\n')
    lineLabel.grid(row=4, column=0)

      
def accept_token():
    global inToken
    global newToken
    my_text3.insert(INSERT, " \naccept token from the list:"+inToken[1] + '\n')
    if(len(newToken) != 0):
        inToken=newToken.pop(0)

def math():
    my_text3.insert(INSERT, "\n----parent node math, finding children nodes:\n")
    global inToken

    my_text3.insert(INSERT, inToken)

    if(inToken[0]=="float"):   

        my_text3.insert(INSERT,"\nchild node (internal): float")
        my_text3.insert(INSERT," \n float has child node (token):"+inToken[1])
        accept_token()

    if (inToken[0]=="int"): 

        my_text3.insert(INSERT,"\nchild node (internal): int")
        my_text3.insert(INSERT,"\nint has child node (token):"+inToken[1])
        accept_token()

        if(inToken[1]=="*"):
            my_text3.insert(INSERT,"\nchild node (token):"+inToken[1])
            accept_token()

            my_text3.insert(INSERT,"\nchild node (internal): math")
            math()
        else:
            my_text3.insert(INSERT,"\nerror, you need + after the int in the math")

    elif (inToken[1]=="+"):
        my_text3.insert(INSERT,"\nchild token (token)" + inToken[1])
        accept_token()

        if(inToken[0]=="int"):
          
          my_text3.insert(INSERT,"\nchild token (internal): math")
          math()
          
          my_text3.insert(INSERT,"\nint has child node (token)"+ inToken[1])
        else:
          my_text3.insert(INSERT,"\nerror, you need an int after +")
    else:
        my_text3.insert(INSERT,"\nerror, math expects float or int")
    
def exp():    
    my_text3.insert(INSERT,"\n----parent node exp, finding children nodes:\n")
    global inToken
    my_text3.insert(INSERT,inToken[0])
    typeT=inToken[0]
    token=inToken[1]
    if(typeT=="keyword"):
        my_text3.insert(INSERT, "\nchild node (internal): keyword")
        my_text3.insert(INSERT,"\nkeyword has child node (token):\n"+token)
        accept_token()
        exp()
    if(typeT=="identifier"):
        my_text3.insert(INSERT, "\nchild node (internal): identifier")
        my_text3.insert(INSERT,"\nidentifier has child node (token):\n"+token)
        accept_token()
    else:
        my_text3.insert(INSERT, "\nexpect identifier as the first element of the expression!\n") #?
        return

    if(inToken[1]=="="):
        my_text3.insert(INSERT,"\nchild node (token):"+inToken[1])
        accept_token()
    else:
        my_text3.insert(INSERT,"\nexpect = as the second element of the expression!")
        return

    my_text3.insert(INSERT,"\nChild node (internal): math")
    math()
    
def if_exp():    
    my_text3.insert(INSERT,"\n----parent node if_exp, finding children nodes:\n")
    global inToken;
    typeT,token=inToken;
    if(token=="if"):
        my_text3.insert(INSERT,"\nchild node (internal): keyword\n")
        my_text3.insert(INSERT,"\nkeyword has child node (token):"+token)
        accept_token()
    else:
        my_text3.insert(INSERT,"expect keyword as the first element of the expression!\n")
        return
    if(inToken[1]=="("):
        my_text3.insert(INSERT,"\nchild node (token):"+inToken[1])
        accept_token()
    else:
        my_text3.insert(INSERT,"\nexpect ( as the second element of the expression!\n")
        return
    my_text3.insert(INSERT,"\nChild node (internal): math\n")
    comparison_exp()
    my_text3.insert(INSERT,"\n----parent node if_exp, finding children nodes:")
    if(inToken[1]==")"):
        my_text3.insert(INSERT,"\nchild node (token):"+inToken[1])
        accept_token()
    else:
        my_text3.insert(INSERT,"\nexpect ) after comparison expression!\n")
        return
    if(inToken[1]==":"):
        my_text3.insert(INSERT,"\nchild node (token):"+inToken[1])
        my_text3.insert(INSERT,"\nParse Tree Building Sucess!!\n")
        accept_token()
    else:
        my_text3.insert(INSERT,"\nexpect : as the last element of the expression!\n")
        return
    
def comparison_exp():
    my_text3.insert(INSERT,"\n----parent node comparison_exp, finding children nodes:\n")
    global inToken;
    typeT,token=inToken;
    my_text3.insert(INSERT,inToken)
    if(typeT=="identifier"):
        my_text3.insert(INSERT,"\nchild node (internal): identifier\n")
        my_text3.insert(INSERT,"\nidentifier has child node (token):"+token)
        accept_token()
        comparison_exp()
    elif(typeT=="operator"):
        my_text3.insert(INSERT,"child node (token):"+inToken[1])
        accept_token()
        comparison_exp()
    else:
        my_text3.insert(INSERT,"\nexpected identifier or operator!\n")
        return
        
def parser(x):
    global inToken
    inToken=x.pop(0)
    exp() 
    if(inToken[1]==";"):
        my_text3.insert(INSERT,"\nparse tree building success!")
        return
    if_exp()
    if(inToken[1]==";"):
        my_text3.insert(INSERT,"\nparse tree building success!")
        return
    
my_text = Text(root, width=30, height=20)
my_text.grid(row=1, column=0)

lineLabel = Label(root, text='Current Processing Line: ' + str(Line))
lineLabel.grid(row=4, column=0)

my_text2 = Text(root, width=30, height=20)
my_text2.grid(row=1, column=5)

quit_button = Button(root, text="Exit", command=quit)
quit_button.grid(row=5, column=7)

next_button = Button(root, text="Next Line", command=next)
next_button.grid(row=5, column=0, padx=20)

my_label = Label(root, text='')
my_label.grid(row=3, column=3)
label1 = Label(root, text='Lexical Analyzed Result:')
label1.grid(row=0, column=5)
label2= Label(root, text='Source Code Input:')
label2.grid(row=0, column=0)
my_label3 = Label(root, text='')
my_label3.grid(row=3, column=6)
my_label4 = Label(root, text='Parse Tree:')
my_label4.grid(row=0, column=7)
my_text3 = Text(root, width=35, height=20)
my_text3.grid(row=1, column=7)

root.mainloop()
