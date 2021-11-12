import PySimpleGUI as psg 
from storyCollection import stories
from utils import get_word_types, finish_story, input_is_valid

# Current story
currentStory = stories[1]

def create_fields():
    '''Create input fields'''

    fields = get_word_types(currentStory)
    listToRender = []
    for field in fields:
        listToRender.append([psg.Text("Enter a(n) {}: ".format(field), font='Courier 14'), psg.Input(size=(50,1), pad=(8, 8), font='Courier 14')])
    return listToRender

def submit_input():
    '''Submit input to complete story'''

    inputs = values_list.values()
    completeStory = finish_story(inputs, currentStory)
    layout = [[psg.Text(completeStory)]]
    window = psg.Window("Your story", layout, modal=True, margins=(150,150),)
    choice = None # make this close
    while True:
        event, values = window.read()
        if event == "End Game" or event == psg.WIN_CLOSED:
            break

    window.close()

libItButton = [[psg.Button("Lib It!", size=(30,1.5), font='Courier 14')]]
endGameButton = [[psg.Button("End Game", size=(30,1.5), font='Courier 14')]]

# Create page layout
layout = [
    [psg.Text("Welcome! Get ready to Lib It!", font='Courier 26', justification='center')],
    *create_fields(),
    [psg.Column(libItButton), psg.Column(endGameButton)]
]

# Create window
window = psg.Window("Madlibs", layout, margins=(200,30), element_justification='center')

# Create an event loop
while True:
    event, values_list = window.read()
    # End program if user closes window or presses the Ok button -- add 
    if event == "End Game" or event == psg.WIN_CLOSED:
        break
    elif event == "Lib It!":
        submit_input()

window.close()
