import text
import renderer

class Person:
    def __init__(self, name="Unnamed", age=0, health=100, knows=[], traits=[], possessions=[], is_player=False, relatives=[], location="Earth"):
        self.name = name
        self.age = age
        self.health = health
        self.knows = knows
        self.traits = traits
        self.possessions = possessions
        self.is_player = is_player
        self.relatives = relatives
        self.location = location
    
    def AdvanceAge(self):
        self.age += 1

class World:
    def __init__(self, time_scale = {"1": "Year"}, locations = {"Placeholder":"Earth"}):
        self.time_scale = time_scale
        self.people = []
        self.locations = locations

if __name__ == "__main__":
    render = renderer.Renderer()
    renderResult = render.showEvent(text.TextData().getText("ui_event").format("Event Text"), [text.TextData().getText("ui_choice").format("1", "Option 1"), text.TextData().getText("ui_choice").format("2", "Option 2"), text.TextData().getText("ui_choice").format("3", "Option 3")], text.TextData().getText("ui_input"))
    print(renderResult)

    # print(text.TextData().getText("ui_header").format("Player Name", "Age", "Health", "Current Location"))
    # print(text.TextData().getText("ui_event").format("Event Text"))
    # print(text.TextData().getText("ui_choice").format("1", "Option 1"))
    # print(text.TextData().getText("ui_choice").format("2", "Option 2"))
    # print(text.TextData().getText("ui_choice").format("3", "Option 3"))
    # input(text.TextData().getText("ui_input"))