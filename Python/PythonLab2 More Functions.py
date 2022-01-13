import re 

def find_pattern(s):
  
  result_string = s + " matches the pattern:" 
  any_match = False 
  
  if re.search("\d", s): 
    print(result_string, "An integer")
    any_match = True
    
  if re.search("^\d+\.\d+$", s):
    any_match = True
    print(result_string, "A float consists of 1 or more digits before and after decimal point")

  if re.search("\b\d+\.\d{2}\b", s):
    any_match = True
    print(result_string, "A float with exactly 2 digits after the decimal point")

  if re.search("^\d*\.\d+f$", s):
    any_match = True
    print(result_string, "A float end with letter f")

  if re.search("[A-Z]+[a-z]+\d+", s):
    any_match = True
    print(result_string, "Capital letters, followed by small case letters, followed by digits")

  if re.search("\d{3}[A-z]{2,}", s):
    any_match = True
    print(result_string, "Exactly 3 digits, followed by at least 2 letters")

  if any_match == False: 
    print(s, "doesn't match any patterns.")

def remove_int(string):
    print("Sentence before removing in at start:", string)
    myregex = re.compile('\d+')
    result = myregex.match(string)
    if (result != None):
      string = string[result.end():]
      print("Sentence after checking for int at start:",string)


test_strings = ["22.11","23","66.7f", "123abcde", "Case44","Happy","78","66.7","yes123","Book111"]
for s in test_strings:
  find_pattern(s)

input_string=input("Enter your string : ") 
remove_int(input_string)

input('Press ENTER to exit')
