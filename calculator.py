from PySimpleGUI import PySimpleGUI as sg

sg.theme("Reddit")
layout = [
    [sg.Text("", size=(15,1), font=("Poppins"), text_color=("black"), key=("output"))],
    [sg.ReadFormButton("1", size=(6,1)),sg.ReadFormButton("2", size=(6,1)),sg.ReadFormButton("3", size=(6,1))],
    [sg.ReadFormButton("4", size=(6,1)),sg.ReadFormButton("5", size=(6,1)),sg.ReadFormButton("6", size=(6,1))],
    [sg.ReadFormButton("6", size=(6,1)),sg.ReadFormButton("7", size=(6,1)),sg.ReadFormButton("8", size=(6,1))],
    [sg.ReadFormButton("9", size=(6,1)),sg.ReadFormButton("0", size=(6,1)),sg.ReadFormButton("c", size=(6,1))],
    [sg.ReadFormButton("+", size=(6,1)),sg.ReadFormButton("-", size=(6,1)),sg.ReadFormButton("*", size=(6,1))],
    [sg.ReadFormButton("/", size=(6,1)),sg.ReadFormButton("Enter", size=(14,1))]
]
answer = ""
result = ""
window = sg.Window("Calculator", layout)

while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'c':
        result = ''
        window.find_element("output").Update(result)
    elif len(result) == 16:
        pass

    elif events == "Enter":
        answer = eval(result)
        answer = str(round(float(answer),3))
        window.find_element("output").Update(answer)
        result = answer
    else:
        result += events
        window.find_element("output").Update(result)
