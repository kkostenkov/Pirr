###!usr/bin/python
#encoding:UTF-8
import time
import webClient
import json
import tkinter

host = "http://127.0.0.1:8888/"

connected = False
pointNames = []#"1", "2", "alfa"]
webErrorList = ['The server couldn\'t fulfill the request.', 'We failed to reach a server.']

def timestamp():
    return "[" + time.strftime("%H:%M:%S") + "] "
    
def send(dummyForBindKey=None):
    """ Either send to COM port or check answer offline """
    if entry.get():
        message = timestamp() + entry.get() + "\n"
        with open("history.txt","a") as f: #closes file automatically
            f.write(message)
        historyText.configure( state="normal")
        historyText.insert(tkinter.END, message)
        historyText.configure( state="disabled")
        entry.delete(0, tkinter.END)
        print ("Send button pressed")
        #checkAnswer(pointNumber, message)
    historyText.yview("moveto",1)

def force_start():
    """ Force connection with server, update available quests """
    global connected
    print ("ForceStart pressed")
    questList = webClient.fetch(host)
    
    if questList in webErrorList:
        connectLight.configure(image=connectOffPic)
        connected = False
        return
    
    connectLight.configure(image=connectOnPic)
    questList = questList.decode("utf-8")
    questList = json.loads(questList)
    connected = True

        
    pointNames = []
    for name in questList:
        pointNames.append(name)
    pointSpinbox.configure(state="normal")
    pointSpinbox.delete(0,tkinter.END)
    pointSpinbox.configure(values=pointNames )
    pointSpinbox.configure(state="readonly")
    
def read_txt_history():
    with open("history.txt", "r") as f: #closes file automatically
        text = f.read()
        #f.close()
    return text

def set_task():
    if connected == False:
        return "Disconnected"
    text = webClient.fetch(host=host, quest=currentPoint.get())
    currentTask.set(text)
    taskText.configure( state="normal")
    taskText.delete ( "1.0", tkinter.END )
    taskText.insert(tkinter.END, text)
    taskText.configure( state="disabled")
    return text

root = tkinter.Tk()
root.title("Пирр")
root.resizable(0,0)
root.minsize(width=350, height=180)

#Chat of GUI
textFrame = tkinter.Frame(root, height=200, width=200)
historyText = tkinter.Text(textFrame, height=4, width=50, padx=10,pady=2, wrap='word')
historyText.insert(tkinter.END, read_txt_history())
historyText.configure( state="disabled")

scrollbar = tkinter.Scrollbar(textFrame, command=historyText.yview, orient="vertical")
historyText.configure(yscrollcommand=scrollbar.set)

entry = tkinter.Entry(textFrame,width=60)
entry.bind("<Return>",send)
sendButton = tkinter.Button(textFrame, command = send, text="Send") 

textFrame.grid(column=0, row=1)
historyText.grid(column=0, row=0, columnspan=2)
scrollbar.grid(column=2, row=0, sticky="NS" )
entry.grid(column=0, row=1)
sendButton.grid(column=1, row=1, columnspan=2)

#Control GUI
controlFrame = tkinter.Frame(root)
connectOnPic = tkinter.PhotoImage( file="on.gif")
connectOffPic = tkinter.PhotoImage( file="off.gif")
connectLight = tkinter.Label(controlFrame, image=connectOffPic)

pointLabel = tkinter.Label(controlFrame, height=2, width=7, relief="groove", text="Point\n Number")
currentPoint = tkinter.StringVar()

currentTask = tkinter.StringVar()

pointSpinbox = tkinter.Spinbox(controlFrame, width=10, values=pointNames,textvariable=currentPoint, command=set_task, state="readonly") # !! должен быть Combobox

sotaPic = tkinter.PhotoImage( file="sota.gif")
sotaLabel = tkinter.Label(controlFrame, image=sotaPic)
forceStartButtonPic = tkinter.PhotoImage( file="forceStartButtonPic.gif")
forceStartButton = tkinter.Button(controlFrame, command=force_start, height=50, width=50, image=forceStartButtonPic)

controlFrame.grid(column=1, row=0, rowspan=2)
pointLabel.grid(column=0, row=0)
pointSpinbox.grid(column=0, row=1)
sotaLabel.grid(column=0, row=2)
connectLight.grid(column=0, row=3)
forceStartButton.grid(column=0, row=4)

# Mission GUI
missionFrame = tkinter.Frame(root)

taskLabel = tkinter.Label(missionFrame, height=1, width=60, relief="groove",text="Task info") #sunken
taskText = tkinter.Text(missionFrame, height=8, width=60, wrap='word')
taskText.insert(tkinter.END, set_task())
taskText.configure( state="disabled")
scrollbar2 = tkinter.Scrollbar(missionFrame, command=taskText.yview, orient="vertical")
taskText.configure(yscrollcommand=scrollbar2.set)

missionFrame.grid(column=0, row=0)
taskLabel.grid(column=0, row=1)
taskText.grid(column=0, row=2)
scrollbar2.grid(column=1, row=2, sticky="NS" )

force_start()
tkinter.mainloop()

