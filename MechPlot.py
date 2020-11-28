import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
import PySimpleGUI as sg 
from matplotlib.ticker import NullFormatter  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')

op = 1
while op==1:
    sg.theme('LightBlue')
    layout_org = [
        [sg.Text("Software to draw Shear Force and Bending Moment diagram",font='Any 20',text_color='White',background_color='DarkBlue')],
        [sg.Text("Based on the provided details SFD and BMD can be drawn for the following case :-",font='Any 16')],
        [sg.Text(" (a) Cantilever beam with multiple point Forces.",font='Any 16')],
        [sg.Text(" (b) Simply Supported beam with multiple point Forces",font ='Any 16')],
        [sg.Text("Select the type of Beam",font='Any 20')],
        [sg.Button("(a) Cantilever",size=(22,2),font='Any 18'),sg.Button("(b) Simply Supported",size=(22,2),font='Any 18')],
        [sg.Text("Project by -")],
        [sg.Text("   Anish Sangrulkar, roll no. 190107068")]
    ]

    window_org = sg.Window("ME212 Project",layout=layout_org)

    while True:
        events,values = window_org.read()
        if events=="(a) Cantilever":
            choice = 1
            break
        elif events=="(b) Simply Supported":
            choice = 2
            break
        elif events==sg.WIN_CLOSED or events==None:
            choice = 0
            break

    window_org.close()

    if choice==2:
        import SC
    elif choice==1:
        import C
    else :
        break
    
 