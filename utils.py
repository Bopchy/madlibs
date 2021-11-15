import re
import storyCollection

def get_word_types(story):
    '''Function for retrieving word types required by story in order of occurrence'''

    wordTypesList = re.findall(r'\{(.*?)\}', story["content"])
    return wordTypesList

def finish_story(userInput, story):
    '''Function to replace required word types with the user input'''

    # Remove words in between curly brackets, replacing them with empty curly brackets that string.format() can act on
    # 'count' restricts substitutions to the length of the userInput array 
    completeStory = re.sub(r'\{(.*?)\}', '{}', story["content"], count=len(userInput))
    # Format string replacing brackets with user input
    return completeStory.format(*userInput)

def input_is_valid(input):
    '''Check if user input is not empty and is a string'''

    if len(input) < 1 or not input.isalpha():
        return False
    return True
