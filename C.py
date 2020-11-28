import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
import PySimpleGUI as sg 

layout1 = [
    [sg.Text("Enter the details for a Cantilever Beam")],
    [sg.Text("Enter length of the beam "),sg.InputText(key='L')],
    [sg.Text("Enter number of point loads "),sg.InputText(key='n')],
    [sg.Button('Next')]
]

window1 = sg.Window("Cantilever Beam",layout=layout1)
while True:
    events,values = window1.read()
    if events == sg.WIN_CLOSED or events == 'Next':
        L = float(values['L'])
        n = int(values['n'])
        break

window1.close()

layout2 = []
for i in range(0,n):
    layout2.append([sg.Text("{}.   ".format(i+1)),sg.Text("Load in N = "),sg.InputText(key="F{}".format(i)),sg.Text("Position of load from left end in m = "),sg.InputText(key="pos{}".format(i))])
layout2.append([sg.Button('Show')])

F=[]
pos = []
window2 = sg.Window("Camtilever Beam",layout=layout2)
while True:
    events,values = window2.read()
    if sg.WIN_CLOSED or events == 'Show':
        for i in range(0,n):
            F.append(float(values["F{}".format(i)]))
            pos.append(float(values["pos{}".format(i)]))
        break

window2.close()

pos.append(L+1)
R=0
M=0
for i in range(0,n):
    R=R+F[i]
    M=M+F[i]*pos[i]

l=np.linspace(0,L,1000)
X=[]
SF=[]
BM=[]
j=0
f=0
b=0
for x in l:
    if x <= pos[j]:
        sf = f-R
        bm = M-b+sf*x
    elif x>pos[j]:
        f=f+F[j]
        b=b+F[j]*pos[j]
        j=j+1
    SF.append(sf)
    BM.append(bm)
    X.append(x)

from matplotlib.ticker import NullFormatter  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')

# Matplotlib code 
plt.figure(figsize=(12,6))
plt.subplot(121)
plt.plot(X, SF)
plt.plot([0, L], [0, 0])
plt.plot([0, 0], [0, SF[0]], [L, L], [0, SF[999]])
plt.title("SFD")
plt.xlabel("Length in m")
plt.ylabel("Shear force in N")

plt.subplot(122)
plt.plot(X, BM)
plt.plot([0, L], [0, 0])
plt.plot([0, 0], [0, BM[0]], [L, L], [0, BM[999]])
plt.title("BMD")
plt.xlabel("Length in m")
plt.ylabel("Bending moment in Nm")
# ------------------------------- Beginning of Matplotlib helper code -----------------------

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# ------------------------------- Beginning of GUI CODE -------------------------------
sg.theme('Light Brown 3')

fig = plt.gcf()  # if using Pyplot then get the figure from the plot
# define the window layout
layout = [[sg.Text('SF and BM diagram for Cantilever beam', font='Any 18')],
          [sg.Canvas(key='-CANVAS-')],
          [sg.Exit()]]

# create the form and show it without the plot
window = sg.Window('Cantilever Beam',
    layout, force_toplevel=True, finalize=True)

# add the plot to the window
fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, fig)

# show it all again and get buttons
event, values = window.read()

window.close()