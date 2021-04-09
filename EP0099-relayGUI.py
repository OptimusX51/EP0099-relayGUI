from tkinter import *
import smbus
import sys

DEVICE_BUS = 1
DEVICE_ADDR = 0x10
bus = smbus.SMBus(DEVICE_BUS)

def pumpfunc():
    if pumpvar.get() == 0:
        bus.write_byte_data(DEVICE_ADDR, 1, 0x00)
        txt1 = 'OFF'
    else:
        bus.write_byte_data(DEVICE_ADDR, 1, 0xFF)
        txt1='ON'
    selection = ("Pump is " + txt1)
    label1.config(text = selection)
    #print(pumpvar.get())

def S1func():
    if S1var.get() == 0:
        bus.write_byte_data(DEVICE_ADDR, 2, 0x00)
        txt1 = 'CLOSED'
    else:
        bus.write_byte_data(DEVICE_ADDR, 2, 0xFF)
        txt1='OPEN'
    selection = ("S1 is " + txt1)
    label2.config(text = selection)

def S2func():
    if S2var.get() == 0:
        bus.write_byte_data(DEVICE_ADDR, 3, 0x00)
        txt1 = 'CLOSED'
    else:
        bus.write_byte_data(DEVICE_ADDR, 3, 0xFF)
        txt1='OPEN'
    selection = ("S2 is " + txt1)
    label3.config(text = selection)

def S3func():
    if S3var.get() == 0:
        bus.write_byte_data(DEVICE_ADDR, 4, 0x00)
        txt1 = 'CLOSED'
    else:
        bus.write_byte_data(DEVICE_ADDR, 4, 0xFF)
        txt1='OPEN'
    selection = ("S3 is " + txt1)
    label4.config(text = selection)
    

root = Tk()
pumpvar = IntVar()
S1var = IntVar()
S2var = IntVar()
S3var = IntVar()
S4var = IntVar()

#Individual relay frames
pump_frame = Frame(root, width=200, height=200)
pump_frame.pack(side='left', fill='both', padx=5, pady=10)
S1_frame = Frame(root, width=200, height=200)
S1_frame.pack(side='left', fill='both', padx=5, pady=10)
S2_frame = Frame(root, width=200, height=200)
S2_frame.pack(side='left', fill='both', padx=5, pady=10)
S3_frame = Frame(root, width=200, height=200)
S3_frame.pack(side='left', fill='both', padx=5, pady=10)

#Pump radiobuttons
labelpump = Label(pump_frame, text='Pump',font='bold',relief=RAISED)
labelpump.pack(anchor = CENTER)
R1 = Radiobutton(pump_frame, text="Pump OFF", variable=pumpvar, value=0,
                  command=pumpfunc)
R1.pack( anchor = W )

R2 = Radiobutton(pump_frame, text="Pump ON", variable=pumpvar, value=1,
                  command=pumpfunc)
R2.pack( anchor= W )
#S1 radiobuttons
labelS1 = Label(S1_frame, text='S1',font='bold',relief=RAISED)
labelS1.pack(ancho = CENTER)
R3 = Radiobutton(S1_frame, text="S1 CLOSED", variable=S1var, value=0,
                  command=S1func)
R3.pack( anchor = W )

R4 = Radiobutton(S1_frame, text="S1 OPEN", variable=S1var, value=1,
                  command=S1func)
R4.pack( anchor = W )
#S2 radiobuttons
labelS2 = Label(S2_frame, text='S2',font='bold',relief=RAISED)
labelS2.pack(ancho = CENTER)
R5 = Radiobutton(S2_frame, text="S2 CLOSED", variable=S2var, value=0,
                  command=S2func)
R5.pack( anchor = W )

R6 = Radiobutton(S2_frame, text="S2 OPEN", variable=S2var, value=1,
                  command=S2func)
R6.pack( anchor = W )
#S3 radiobuttons
labelS3 = Label(S3_frame, text='S3',font='bold',relief=RAISED)
labelS3.pack(ancho = CENTER)
R7 = Radiobutton(S3_frame, text="S3 CLOSED", variable=S3var, value=0,
                  command=S3func)
R7.pack( anchor = W )

R8 = Radiobutton(S3_frame, text="S3 OPEN", variable=S3var, value=1,
                  command=S3func)
R8.pack( anchor = W )


label1 = Label(pump_frame)
label1.pack()
label2 = Label(S1_frame)
label2.pack()
label3 = Label(S2_frame)
label3.pack()
label4 = Label(S3_frame)
label4.pack()
root.mainloop()
