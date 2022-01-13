#Python lab 1
#Learn from the online interactive tutorial and finish below tasks
#You can edit in this file by filling blanks after each question.
#Submit the .py file for your own reference
#This practice is graded only on submission. 
#It will help you to get started on Python for the homework

#####
#Example function
#####
def example(): #def is function definition
    print("I am the example code")
#Now, go to the end of this file and you will find the main function & how to run your code there
#Around line #94


#####
#1. function in python
####

def printHello(): #Remove the # at the begining of this line.
    print("hello world")
    #tab is IMPORTANT in python. tab in python replaces {} in C++
    #print string hello world. One line of code here. Make sure it is indented to show it belongs to this function


#####
#2. variable definition in python
#####

def someVars():
    num = 5
    num2 = 15
    flo = 5.5
    flo2 = 25.5
    print(flo + flo2 + num + num2)
    #define a few integer and float numbers, add them together and print result out

#call the function to run it in the main function at the end of the file



#####
#2.5. if elif if and input in python
#####
def input_if():
    #read a number from the user
    num = int(input("Enter a number"))
    #say hi if positive, say hello if negative, or say yo if 0
    if num > 0:
      print ("hi")
    elif num < 0:
      print ("hello")
    else: 
      print ("yo")
#call the function to run it in the main function at the end of the file


#####
#3. define a list in python
#####

def mylis():
    #define a list with 5 numbers, print it out
    thislist = [1,2,3,4,5]
    print(thislist)
    #define an empty list and append a few numbers into it, then print it out
    thatlist = []
    thatlist.append(1)
    thatlist.append(22)
    thatlist.append(333)
    print(thatlist)

#call your mylis func to execute in the main function at the end of the file

#####
#4. string output
#####

def printstr(input_str1, input_int1):
    #convert int into string and append the int with the string to form a long string
    str2 = str(input_int1)
    str3 = input_str1 + str2
    print(str3)
    #(technical googling practice -- google what func to use)
    #print the long str out

#In the main function, define an input string and an input int.
#Pass them in as parameters to the function. Call and run the function to see results.

####
#5. passing var to func and return
####

def funcvars(inputvar1, inputvar2):
    #add the input numbers together
    sum = inputvar1 + inputvar2
    #returen the result
    print(sum)
#Define the input variables in main, pass them into the function.
#In main, use a result variable to receive the result from funcvars and print the result out

####
#6. for loop
####

def go_over_list(mylis):
    #use for loop to go over the input list and print out items one by one
    for i in mylis:
      print(i)

def go_over_list1():
    #use for loop to directly print out numbers from 10 to 17
    list1 = [10, 11, 12, 13, 14, 15, 16, 17]
    for i in list1:
      print(i)

def go_over_list2(mylis):
    #use for loop & go over your list
    for i in mylis:
    #multiply 2 to every item in your list, print results out
      print(i * 2)

def go_over_list3(mylis):
    #create an empty list resLis
    resLis = []
    #go over items in the input list, multiply 2 to every item
    for i in mylis:
      sum = i * 2
      resLis.append(sum)
    #add result one by one to resLis
    for i in resLis:
      print(i)
    #return resLis

#Call all the functions in main. Provide necessary inputs to the functions.
#For those with return values, print the return values out in main.

####
#7. while loop
####
def whilelist(mylis):
  newList = []
  for i in mylis:
    newList.append(i)
  i = 0;
  while i < len(newList): 
    print(newList[i])
    i += 1;

def whilelist1():
  list1 = [10, 11, 12, 13, 14, 15, 16, 17]
  i = 0;
  while i < (len(list1)):
    print(list1[i])
    i += 1;

def whilelist2(mylis):
  newList = []
  for i in mylis:
    newList.append(i)
  i = 0;
  while i < len(newList): 
    print(newList[i] * 2)
    i += 1;

def whilelist3(mylis):
  newList = []
  newList2 = []
  for i in mylis:
    newList.append(i)
  i = 0;
  while i < len(newList): 
    newList2.append(newList[i] * 2)
    i += 1;
  i = 0;
  while i < len(newList2):
    print(newList2[i])
    i += 1;
#do all the problems in 6 using while loop instead


#####
#Here is the main function
#You can have only 1 main function in 1 script
#Left click on the green arrow next to the line number of the line of the main function definition
#Your code would run.
if __name__ == '__main__': #a quick way to type this line is: type "main" and then tab
   print("****Example****")
   example()
   print("****Question 1****")
   printHello()
   print("****Question 2****")
   someVars()
   print("****Question 2.5****")
   input_if()
   print("****Question 3****")
   mylis()
   print("****Question 4****")
   printstr("haha", 101)
   print("****Question 5****")
   result = funcvars(5, 10)
   print(result)
   print("****Question 6****")
   list0 = [1, 3, 5, 7 ,9]
   go_over_list(list0)
   go_over_list1()
   go_over_list2(list0)
   go_over_list3(list0)
   print("****Question 7****")
   whilelist(list0)
   whilelist1()
   whilelist2(list0)
   whilelist3(list0)

    #you can start call and run your functions here


######
#Python is an easier PL to learn than C++ and looks like C++
#From this lab experience, reflect and summary what it feels like
#when you are learning a new PL that is similar to a PL that you already know? 
#Your answer here: It's a lot easier to pick up, at least the basics. It took quite a bit longer to learn the same basics when I was learning C++ for the first time.

#In this case, when you want to learn a new PL that looks like a PL that you already know,
#how can you learn the new PL quickly? Any steps?
#Your answer here: I learned it off of basically google only, and clicking the sites that match what I want to know. Lots of repeating this, as it took quite a bit of searching to find everything I wanted to know.
input('Press ENTER to exit')
