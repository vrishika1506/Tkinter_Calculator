GUI CALCULATOR APPLICATION


A tkinter-based desktop application

what is tkinter?

Tkinter is python's built-in library for creating graphical user interface(GUI) applications.

it provides widgets like window,button,entry,label,etc..

it follows an event-driven programming model(code runs when a user clicks the button).

Purpose of this program:

creates a calculator GUI

allow user to:

        enter numbers and operators

        perform arithmetic calculations

        clear the input

uses python's eval() function to evaluate mathematical expressions.
KEY CONCEPTS USED:

    CONCEPT                            DESCRIPTION

    TKinter widgets                 Tk,entry,button

    event handling                  button clicking actions

    lambda functions                passing button values

    grid layout                     positioning UI elements

    exception handling              handling invalid expressions

import tkinter as tk

'''imports tkinter module,tk is an alias for easy access'''

def press(v):
  entry.insert(tk.END,v)
  '''called when a number or operator button is clicked.Inserts the pressed value at the end of entry widget'''

def clear():
  entry.delete(0,tk.END)
  '''clears the calculator screen,deletes all characters from index 0 to end'''

def calc():
  try:
    result=eval(entry.get())
    '''entry.get() retrives the expression(eg:5+3),eval() evaluates the string as a python expression'''
    entry.delete(0,tk.END) #clears the screen
    entry.insert(0,result) # displays the result

  except:
    entry.delete(0,tk.END)
    entry.insert(0,"Invalid Expression")
    '''handles invalid expression(eg.5++),display appropriate message instead of crashing'''

#main window creation
root=tk.Tk() #creates the main application window
root.title("Calculator")#sets the title of the window

root.configure(bg="#1e1e1e") #sets background color of the window
root.resizable(False, False) #prevents or disable resizing of the window

#entry widget creation(display screen of the calculator)
entry=tk.Entry(
  root,
  width=16,
  font=('Arial',24),
  bg="#333333",
  fg="#ffffff",
  bd=0,
  justify="right"
  )

''''text input field
It acts as calcualtor display,right-aligned for better calculator look'''
entry.grid(row=0,column=0,columnspan=4,padx=12,ipady=10)
'''places entry at top,columnspan=4 makes it span across 4 columns,
padx adds horizontal padding,ipady adds internal vertical padding'''

#button labels creation

buttons=[
  '7','8','9','/',      
  '4','5','6','*',
  '1','2','3','-',
  '0','.','=','+'
  ]
'''represent calculator buttons,stored in a list to reduce repetitive code'''

#dynamic button creation 

r=1
c=0
'''rows and column counters for grid layout'''

for b in buttons:
  cmd=calc if b=='=' else lambda x=b: press(x)
  '''if button is '=' call  calc() function to cmd,
  else call press() with button label lambda x=b prevnts late binding issue'''
  tk.Button(
    root,
    text=b,
    command=cmd,
    width=5,
    height=2,
    font=('Arial',18),
    bg="#333333" if b in "+-*/=" else "#4d4d4d",
    fg="#ffffff",
    bd=0,
  ).grid(row=r,column=c,padx=2,pady=2)
  c+=1
  if c==4:
    r+=1
    c=0
    '''moves to next row after 4 buttons'''

#clear button creation
tk.Button(
  root, 
  text='C',
  command=clear,
  width=22, 
  height=2,
  font=('Arial',18),
  bg="#ff3333",
  fg="#ffffff",
  bd=0,
).grid(row=r,column=0,columnspan=4,pady=8)
'''clear button spans all 4 columns at the bottom'''
#start the main event loop
root.mainloop()
'''keeps the application running,waiting for user interaction'''
