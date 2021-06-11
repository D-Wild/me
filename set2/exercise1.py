"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# This will declare a variable some words and it'll put a list of strings
some_words = ['what', 'does', 'this', 'line', 'do', '?']
# This will print the words in the previous list
for word in some_words:
    print(word)
# This will print the words in the previous list
for x in some_words:
    print(x)
# This will print the all the words in the previous list
print(some_words)
# print the words depending on the length
if len(some_words) > 3:
    print('some_words contains more than 3 words')
# prints computer stats
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
