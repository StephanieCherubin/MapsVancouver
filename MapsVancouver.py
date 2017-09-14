#----------------------------------------------
#Vancouver Maps
#----------------------------------------------

#import the modules we need, for creating a GUI
import tkinter

#only press return once
okToPressReturn = True

#the player's attributes.
time = 40

#-------------------------------------------------------------------

def startAnimation(event):

    global okToPressReturn

    if okToPressReturn == False:
        pass
    
    else:
        #update the time left label.
        startLabel.config(text="")
        #start updating the values
        updateTime()
        updateDisplay()

        okToPressReturn = False

#-------------------------------------------------------------------
 
def updateDisplay():

    #use the globally declared variables above.
    global time

    if time<=40 and time>30:
        mapPic.config(image = Vancouver1)
    elif time<=30 and time>20:
        mapPic.config(image = Vancouver2)
    elif time<=20 and time>10:
        mapPic.config(image = Vancouver3)    
    elif time<=10:
        mapPic.config(image = Vancouver4)

    #update the time left label.
    timeLabel.config(text="Time: " + str(time))

    #run the function again after 100ms.       
    mapPic.after(100, updateDisplay)

#-------------------------------------------------------------------
 
def updateTime():

    #use the globally declared variables above.
    global time

    #decrement the time.
    time -= 1

    if isAlive():
        #run the function again after 100ms.
        timeLabel.after(100, updateTime)

#-------------------------------------------------------------------

def feed():

    global time
    
    if time <= 15:
        time += 10
    else:
        time -=10
        
#-------------------------------------------------------------------

def isAlive():

    global time
    
    if time <= 0:
        #update the start info label.
        startLabel.config(text="End")     
        return False
    else:
        return True


def close_window():
    import sys
    sys.exit()        
#-------------------------------------------------------------------


#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("VancouverMap!")
#set the size.
root.geometry("600x600")

#add a label for the start text.
startLabel = tkinter.Label(root, text="Press 'Return/Enter' to start!", font=('Helvetica', 12))
startLabel.pack()

#add a time label.
timeLabel = tkinter.Label(root, text="Time: " + str(time), font=('Helvetica', 12))
timeLabel.pack()

Vancouver1 = tkinter.PhotoImage(file="Vancouver Census-Median Cost of Housing.png")
Vancouver2 = tkinter.PhotoImage(file="Vancouver Census-Median Cost of Housing2.png")
Vancouver3 = tkinter.PhotoImage(file="Vancouver Census-Median Cost of Housing3.png")
Vancouver4 = tkinter.PhotoImage(file="Vancouver Census-Median Cost of Housing4.png")

#add an image
mapPic = tkinter.Label(root, image=Vancouver1)
mapPic.pack()

buttonFeed = tkinter.Button(root, text="Next map", font = "Arial", bg = "gray", fg = "black", activebackground="white",
                            activeforeground="black", width=20, command=feed)
buttonFeed.pack()

buttonEnd = tkinter.Button (root, text="Goodbye", fg = "black", bg = "gray", activebackground="lightblue", 
                            font = "Arial", activeforeground="black",width=10, command=close_window)
buttonEnd.pack()

#run the 'startAnimation' function when the enter key is pressed.
root.bind('<Return>', startAnimation)

#start the GUI
root.mainloop()