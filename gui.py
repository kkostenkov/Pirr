import tkinter

connected = False

def send(dummyForBindKey=None):
    """ Either send to COM port or check answer offline """
    if entry.get():
        message = str(entry.get()+ "\n")
        f = open("history.txt","a") 
        f.write(message)
        f.close()
        historyText.configure( state="normal")
        historyText.insert(tkinter.END, message)
        historyText.configure( state="disabled")
        entry.delete(0, tkinter.END)
        print ("Send button pressed")

        #netSend(message) 
        #checkAnswer(pointNumber, message)
    historyText.yview("moveto",1)

def force_start():
    """ Force connection with another station """
    global connected
    print ("ForceStart pressed")
    if connected == True:
        connectLight.configure(image=connectOffPic)
        connected = False
        return
    connectLight.configure(image=connectOnPic)
    connected = True

def read_txt_history():
    f = open("history.txt", "r")
    text = f.read()
    f.close()
    return text

root = tkinter.Tk()
root.title("Пирр")
root.resizable(0,0)
root.minsize(width=350, height=180)

#Left side of GUI
textFrame = tkinter.Frame(root, height=200, width=200)
historyText = tkinter.Text(textFrame, height=8, width=30, padx=10,pady=10, wrap='word')
historyText.insert(tkinter.END, read_txt_history())
historyText.configure( state="disabled")
scrollbar = tkinter.Scrollbar(textFrame, command=historyText.yview, orient="vertical")
historyText.configure(yscrollcommand=scrollbar.set)
entry = tkinter.Entry(textFrame,width=40)
entry.bind("<Return>",send)
sendButton = tkinter.Button(textFrame, command = send, text="Send") 

textFrame.grid(column=0, row=0)
historyText.grid(column=0, row=0, columnspan=2)
scrollbar.grid(column=2, row=0, sticky="NS" )
entry.grid(column=0, row=1)
sendButton.grid(column=1, row=1, columnspan=2)

#Right side of GUI
controlFrame = tkinter.Frame(root)
connectOnPic = tkinter.PhotoImage( file="on.gif")
connectOffPic = tkinter.PhotoImage( file="off.gif")
connectLight = tkinter.Label(controlFrame, image=connectOffPic)
pointInfo = tkinter.Label(controlFrame, height=1, width=15, relief="groove", text="Point Number")
pointList = tkinter.Listbox(controlFrame, height=1, width=5) # !! должен быть Combobox
pointList.insert(tkinter.END, "a","b")

taskInfo = tkinter.Label(controlFrame, height=1, width=15, relief="groove",text="Task info") #sunken
sotaPic = tkinter.PhotoImage( file="sota.gif")
sotaLogo = tkinter.Label(controlFrame, image=sotaPic)
forceStartButtonPic = tkinter.PhotoImage( file="forceStartButtonPic.gif")
forceStartButton = tkinter.Button(controlFrame, command=force_start, height=50, width=50, image=forceStartButtonPic)

controlFrame.grid(column=1, row=0)
sotaLogo.grid(column=1, row=0)
pointInfo.grid(column=0, row=1)
pointList.grid(column=1, row=1)
taskInfo.grid(column=0, row=2)
connectLight.grid(column=0, row=0)
forceStartButton.grid(column=1, row=3)

tkinter.mainloop()
