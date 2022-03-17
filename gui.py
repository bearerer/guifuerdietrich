#!/usr/bin/python3

import PySimpleGUI as sg

layout = [[sg.Text("Hallo Dietrich")], [sg.Button("OK")]]

# Create the window
window = sg.Window("HalloDietrich", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
