import re
def cutOneLineTokens(line):
  newLine="["
  while 1:
    line=line.strip()
        
    if len(line)==0:
        break
    x=re.match(r"(=|\+|>|\*)",line)
    if x is not None:
        newLine+=f'<"op",{x.group()}>,'
        line=line[:x.span()[0]]+line[x.span()[1]:]
    x=re.match("(if|int|else|float)",line)
    if x is not None:
        newLine+=f'<"key",{x.group()}>,'
        line=line[:x.span()[0]]+line[x.span()[1]:]
    x=re.match(r"(\(|\)|:|\"|;)",line)
    if x is not None:
        newLine+=f'<"seperator",{x.group()}>,'
        line=line[:x.span()[0]]+line[x.span()[1]:]
    x=re.match(r"\d+\.\d+",line)
    if x is not None:
        newLine+=f'<"float",{x.group()}>,'
        line=line[:x.span()[0]]+line[x.span()[1]:]
    x=re.match(r"(\d+)",line)
    if x is not None:
        newLine+=f'<"lit",{x.group()}>,'
        line=line[:x.span()[0]]+line[x.span()[1]:]
    x=re.match(r"\w([a-zA-z0-9])*",line)
    if x is not None:
        newLine+=f'<"id",{x.group()}>,'
        line=line[:x.span()[0]]+line[x.span()[1]:]
                        
  newLine=newLine[:-1]
  newLine+="]"
  print(newLine)
  if(line == ""):
      print("...")

tokenLine = input("Test Input String: ")
cutOneLineTokens(tokenLine)

    
