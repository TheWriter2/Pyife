class TextData:
    def __init__(self):
        self.text_data = {
            "ui_simple": "{}",
            "ui_header": "{} | Age: {} | Health: {} | {}\n",
            "ui_event": "Event: {}\n\nWhat will you do:",
            "ui_choice": "{}. {}",
            "ui_input": "\nType something then press enter to continue: "
        }
    
    ### Gets text from TextData entry ###
    def getText(self, entry):
        return self.text_data[entry]