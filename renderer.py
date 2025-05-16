import os

class Renderer:
    def __init__(self):
        pass

    def showEvent(self, eventTitle, choices, inputText):
        print("\n" + eventTitle + "\n")
        for i in choices:
            print(i)
        
        return input("\n" + inputText)