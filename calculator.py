import tkinter as tk

'''imports tkinter module,tk is an alias for easy access'''

def press(v):
  entry.insert(tk.END,v)
  '''called when a number or operator button is clicked.Inserts the pressed value at the end of entry widget'''

def clear():
  entry.delete(0,tk.END)
  '''clears the calculator screen,deletes all characters from index 0 to end'''
  
def backspace():
  current_text=entry.get()
  entry.delete(0,tk.END)
  entry.insert(0,current_text[:-1])
  '''removes the last character from the entry widget'''

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

#Main window creation
root=tk.Tk()  #Creates the main application window
root.title("Simple Calculator")  #Sets the title of the window
root.config(bg="#1e1e1e")  #Sets the background color of the window
root.resizable(0,0)  #Prevents resizing of the window

#Entry widget creation
entry=tk.Entry(
  root,
  font=('Times New Roman',20),
  bg="#2d2d2d",
  fg="white",
  bd=0,
  justify='right'
  )
''' Text input field
Acts as calculator display
Right-aligned for better calculator look'''
entry.grid(row=0,column=0,columnspan=4,pady=10)
#Places the entry widget in the grid layout at row 0,column 0,spanning 4 columns with vertical padding of 10 pixels

#Button creation
buttons=[
  '7','8','9','/',
  '4','5','6','*',
  '1','2','3','-',
  '0','.','=','+'
  ]
'''Represent calculator buttons in a list to reduce repetive code'''

#Dynamic button creation
row_val=1
col_val=0
for button in buttons:
  cmd = calc if button=='=' else lambda x=button: press(x)
  '''if button is '=',assign calc function to cmd'''
  '''otherwise, call press() with button value lambda x=button prevents late binding issue'''
  tk.Button(
    root,
    text=button,
    font=('calibri',14),
    bg="#ff9500" if button in {'/','*','-','+','='} else "#333333",
    fg="white",
    bd=0,
    width=5,
    height=2,
    command=cmd
    ).grid(row=row_val,column=col_val,padx=6,pady=6)
  col_val+=1
  if col_val==4:
    row_val+=1
    col_val=0
    '''moves to next row after every 4 buttons'''

#Clear button creation
tk.Button(
  root,
  text="C",
  font=('calibri',14),
  bg="#ff3b3b",
  fg="white",
  bd=0,
  width=10,
  height=2,
  command=clear
).grid(row=row_val,column=0,columnspan=2,pady=8)

#Backspace button creation
tk.Button(
  root,
  text="<-",
  font=('calibri',14),
  bg="#ff3b3b",
  fg="white",
  bd=0,
  width=11,
  height=2,
  command=backspace
).grid(row=row_val,column=2,columnspan=2,pady=8)
'''Creates a clear button that spans all 4 columns in the last row'''

#Start the main event loop
root.mainloop()
'''Starts the Tkinter event loop,waiting for user interaction'''