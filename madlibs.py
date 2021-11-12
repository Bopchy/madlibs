import PySimpleGUI as psg 
from storyCollection import stories
from utils import get_word_types, finish_story, input_is_valid

# Current story
currentStory = stories[1]

# Create input fields
def create_fields():
    fields = get_word_types(currentStory)
    listToRender = []
    for field in fields:
        listToRender.append([psg.Text("Enter a(n) {}: ".format(field)), psg.In()])
    return listToRender

# Submit input to complete story
def submit_input():
    inputs = values_list.values()
    completeStory = finish_story(inputs, currentStory)
    print(completeStory)
    layout = [[psg.Text(completeStory)]]
    window = psg.Window("Your story", layout, modal=True)
    choice = None # make this close
    while True:
        event, values = window.read()
        if event == "End Game" or event == psg.WIN_CLOSED:
            break

    window.close()

# Create page layout
layout = [
    [psg.Text("Madlibs Game")],
    [psg.Button("End Game")],
    *create_fields(),
    [psg.Button("Lib It!")],
]

# Create window
window = psg.Window("Madlibs", layout, margins=(500,400))

# Create an event loop
while True:
    event, values_list = window.read()
    # End program if user closes window or presses the Ok button -- add 
    if event == "End Game" or event == psg.WIN_CLOSED:
        break
    elif event == "Lib It!":
        submit_input()

window.close()
