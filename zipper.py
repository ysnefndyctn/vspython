import FreeSimpleGUI as sg

label1 = sg.Text(" Select file to comprass    ")
input1 = sg.Input()
choose_botton1 = sg.FilesBrowse("Choose")

label2 = sg.Text(" Select Destination Folder ")
input2=sg.Input()
choose_botton2=sg.FolderBrowse("Choose")

compress_button=sg.Button("ComPress")
window=sg.Window("File compressor", layout=[[label1,input1,choose_botton1],
                                                [label2,input2,choose_botton2],
                                                [compress_button]])
window.read()
window.close()