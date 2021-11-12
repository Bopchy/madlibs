import PySimpleGUI as psg 
from storyCollection import stories
from utils import get_word_types, finish_story, input_is_valid

# Current story
currentStory = ""

def pick_story():
    '''Create interface to pick a story to complete'''

    allStories = stories.values()
    storyTitles = []
    for story in allStories:
        storyTitles.append([psg.Button("{}".format(story["title"]))])
    layout = [*storyTitles]
    return layout

def create_fields(story):
    '''Create input fields'''

    fields = get_word_types(story)
    listToRender = []
    for field in fields:
        listToRender.append([psg.Text("Enter a(n) {}: ".format(field)), psg.In()])
    return listToRender

def submit_input():
    '''Submit input to complete story'''

    inputs = values_list.values()
    completeStory = finish_story(inputs, currentStory)
    layout = [[psg.Text(completeStory)]]
    window = psg.Window("Your story", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "End Game" or event == psg.WIN_CLOSED:
            break

    window.close()

def show_input_fields(story):
    '''Create page layout'''

    layout = [
        [psg.Text("Madlibs Game")],
        [psg.Button("End Game")],
        *create_fields(story),
        [psg.Button("Lib It!")],
        [psg.Button("Pick a New Story")],
    ]
    return layout

#  Use global variable to switch layouts
layout = pick_story()

# Create window
window = psg.Window("Madlibs", layout, margins=(400,300))

# Create an event loop
while True:
    event, values_list = window.read()

    if event == "End Game" or event == psg.WIN_CLOSED:
        # End program if user closes window or presses the Ok button
        break
    elif (event == "A really Story" or event == "My Dream Man" or event == "Love Letter" or event == "How to wash your face"):
        # Load user input required for the chosen story
        for story in stories.values():
            if story["title"] == event:
                currentStory = story

        layout = show_input_fields(currentStory)
        window.extend_layout(window, [[psg.Text("Madlibs Game")],
        [psg.Button("End Game")],
        *create_fields(story),
        [psg.Button("Lib It!")],
        [psg.Button("Pick a New Story")]])
    elif event == "Pick a New Story":
        # Go back to the "Pick a story" screen
        # make buttons invisilble above then visible again here 
        layout = pick_story()
    elif event == "Lib It!":
        submit_input()

window.close()
