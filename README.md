# Madlibs - A Python GUI project 

## Technical workflow
This madlibs project relies on the use of Python's string manipulation, Regex and PySimpleGUI to create an interface.

The projects three main files are:
    - _storyCollection.py_
This file contains an object of the stories available to the app. Note that the expected word types to be entered by the user are inside curly braces(`{}`).

    - _utils.py_
This contains the string manipulation and validation functions. Namely:
- get_word_types(story)
  
  Uses regex to find all of the word types (i.e. adverbs, nouns, verbs) that a user needs to enter to complete a story. It then extracts them into a list that is presented to PySimpleGUI, so that the GUI can render the necessary user input fields.

    - `story` is a story from _storyCollection.py_

- finish_story(userInput, story)
  
  Accepts an array of the user input, then uses regex and string formatting to replace all of the expected word types in curly braces with the corresponding user input.

    - `userInput` is an array of the values entered by the user via the GUI
    - `story` is a story from _storyCollection.py_

- input_is_valid(input)

  Checks if `input` is an empty string, or a string that contains numbers.  
  
- _madlibs.py_

    Renders the PySimpleGUI. Note that the input fields are dynamically rendered from a list of expected word types.

## WIP
The following functionalities are still a work in progress:
- Validating the user input
  The input_is_valid() function discussed above is currenlty not in use. The plan is to validate input when the `Lib It!` button is clicked, and if erroneous; an error message will be displayed.
- Generate buttons for different stories, allowing user to pick the one they want
  For this, the plan is to increase the number of stories in the `storyCollection.py` file, then use a function to pull out the titles. Then, dynamically render the titles as buttons that a user can use to pick a story on the landing page of the app.
- Add a `New Game` button
  This would take the user back to the landing page of the app, and allow them to pic a new story. 
- Add tests
