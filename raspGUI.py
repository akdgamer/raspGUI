import tkinter as tk
import tkinter.font as font
import RPi.GPIO as GPIO
import time

# WINDOW INITIALIZATION
root = tk.Tk()
root.geometry("1280x720")

#GPIO Setup
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(10, GPIO.IN)
    
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, True)
# pull_up_down = GPIO.PUD_UP
# GPIO FLUSH

def endprogram():
    GPIO.output(24, False)
    GPIO.cleanup()

#LED FUNCTION

def ledON():
    print("LED button pressed")
    if GPIO.input(18):
        GPIO.output(18, GPIO.LOW)
        ledButton["text"] = "LED ON"
        c.itemconfig(wireIND, fill = 'green')
    else:
        GPIO.output(18, GPIO.HIGH)
        ledButton["text"] = "LED OFF"
        c.itemconfig(wireIND, fill = 'red')

# MAIN FRAME OF THE GUI

mainFrame = tk.Frame(root, width = 1280, height = 720)
mainFrame.pack()

# FONT INITIALIZATION

headFont = font.Font(size = 40)
labelFont = font.Font(size = 30)

# HEADING 

head = tk.Label(mainFrame, text = "WIRE TESTING MACHINE")
head['font'] = headFont
head.place(x = 350, y = 20)

# INDICATOR LABELING

wireLabel = tk.Label(mainFrame, text = "WIRE")
wireLabel['font'] = labelFont
wireLabel.place(x = 150, y = 125 )

capLabel = tk.Label(mainFrame, text = "CAPACITOR")
capLabel['font'] = labelFont
capLabel.place(x = 530, y = 125 )

alarmLabel = tk.Label(mainFrame, text = "ALARM")
alarmLabel['font'] = labelFont
alarmLabel.place(x = 1000, y = 125 )

# CANVAS FOR INDICATOR ICONS

c = tk.Canvas(mainFrame, width = 1500, height = 400) 
c.place(x = 0, y = 200)
wireIND = c.create_oval(75, 20 ,325, 250, fill = 'green')
capIND = c.create_oval(525, 20 ,765, 250, fill = 'green')
alarmIND = c.create_oval(965, 20 ,1215, 250, fill = 'red')

# INFORMATION LABELS

prodLabel = tk.Label(mainFrame, text = "Production - ")
prodLabel['font'] = labelFont
prodLabel.place(x = 100, y = 470)

prodNum = tk.Label(mainFrame, text = "0")
prodNum['font'] = labelFont
prodNum.place(x = 350, y = 470)

modelLabel = tk.Label(mainFrame, text = "Model No. - ")
modelLabel['font'] = labelFont
modelLabel.place(x = 800, y = 470)

modelNum = tk.Label(mainFrame, text = "0")
modelNum['font'] = labelFont
modelNum.place(x = 1050, y = 470)

passLabel = tk.Label(mainFrame, text = "PASS - ")
passLabel['font'] = labelFont
passLabel.place(x = 100, y = 570)

passNum = tk.Label(mainFrame, text = "0")
passNum['font'] = labelFont
passNum.place(x = 300, y = 570)

failLabel = tk.Label(mainFrame, text = "FAIL - ")
failLabel['font'] = labelFont
failLabel.place(x = 100, y = 670)

failNum = tk.Label(mainFrame, text = "0")
failNum['font'] = labelFont
failNum.place(x = 300, y = 670)

# LED BUTTON

ledButton = tk.Button(mainFrame, text = "LED ON", font = labelFont, command = ledON, height = 2, width = 8)
ledButton.place(x = 400, y = 570)

# GPIO OUT TEST



def loop():

    while 1:
        print(GPIO.input(10))
    
    if GPIO.input(10):
        GPIO.output(24, False)
        print(GPIO.input(10))
        print("ON")
    else:
        GPIO.output(24, True)
        print(GPIO.input(10))
        print("OFF")

if __name__ == '__main__':
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        print("KEYBOARD INTERRUPT")
        endprogram()

root.mainloop()
