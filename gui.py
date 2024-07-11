import functions
import FreeSimpleGUI as sg

label= sg.Text(" Type in a to-do ")
input_box = sg.InputText(tooltip="Enter a to-do")
add_Button = sg.Button("Add")

window = sg.Window('My To-do App', layout=[[label],[add_Button,input_box]])
window.read()
window.close()
