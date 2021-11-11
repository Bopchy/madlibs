import re
import storyCollection

# Function for retrieving word types required by story in order of occurrence
def get_word_types(story):
    wordTypesList = re.findall(r'\{(.*?)\}', story["content"])
    return wordTypesList

# Function to replace required word types with the user input
def finish_story(userInput, story):
    # Remove words in between curly brackets, replacing them with empty curly brackets that string.format() can act on
    # 'count' restricts substitutions to the length of the userInput array 
    completeStory = re.sub(r'\{(.*?)\}', '{}', story["content"], count=len(userInput))
    # Format string replacing brackets with user input
    return completeStory.format(*userInput)

# Check if user input is not empty and is a string
def input_is_valid(input):
    if len(input) < 1 or not input.isalpha():
        return False
    return True
