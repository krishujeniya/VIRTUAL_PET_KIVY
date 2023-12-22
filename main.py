from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty

kv_string = '''
BoxLayout:
    orientation: "vertical"

    MDBoxLayout:
        orientation: "horizontal"

        MDIcon:
            icon: "stomach"
            halign: "center"
            font_size: "24sp"
            pos_hint:{'center_x':0.5,'center_y':0.55}                         


        MDProgressBar:
            id: hunger_progress_bar
            value: app.pet.hunger
            max: 100
            pos_hint:{'center_x':0.5,'center_y':0.55}                         


        MDLabel:
            text: app.hunger_percentage
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.55}                         
                      


        MDIcon:
            icon: "emoticon-happy"
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.55}                         


        MDProgressBar:
            id: happiness_progress_bar
            value: app.pet.happiness
            max: 100
            pos_hint:{'center_x':0.5,'center_y':0.55}                         

        MDLabel:
            text: app.happiness_percentage
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.55}                         


        MDIcon:
            icon: "battery"
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.55}                         


        MDProgressBar:
            id: energy_progress_bar
            value: app.pet.energy
            max: 100
            pos_hint:{'center_x':0.5,'center_y':0.55}                         

        MDLabel:
            text: app.energy_percentage
            halign: "center"
            pos_hint:{'center_x':0.5,'center_y':0.55}                         


    MDBoxLayout:
        orientation: "horizontal"
        spacing: "12dp"

        MDRaisedButton:
            text: "Feed"
            icon: "food"
            on_release: app.feed()
            size_hint_x: None
            width: "120dp"
            font_size: "18sp"
            padding: "10dp", "10dp"

        MDRaisedButton:
            text: "Play"
            icon: "gamepad"
            on_release: app.play()
            size_hint_x: None
            width: "120dp"
            font_size: "18sp"
            padding: "10dp", "10dp"

        MDRaisedButton:
            text: "Sleep"
            icon: "sleep"
            on_release: app.sleep()
            size_hint_x: None
            width: "120dp"
            font_size: "18sp"
            padding: "10dp", "10dp"

        MDRaisedButton:
            text: "Exercise"
            icon: "dumbbell"
            on_release: app.exercise()
            size_hint_x: None
            width: "120dp"
            font_size: "18sp"
            padding: "10dp", "10dp"


'''

class VirtualPetApp(MDApp):

    hunger_percentage = StringProperty()
    happiness_percentage = StringProperty()
    energy_percentage = StringProperty()

    def build(self):
        self.title = "Virtual Pet"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        self.pet = VirtualPet()
        self.root = Builder.load_string(kv_string)
        self.update_progress_bars()
        return self.root

    def feed(self):
        self.pet.feed()
        self.update_progress_bars()

    def play(self):
        self.pet.play()
        self.update_progress_bars()

    def sleep(self):
        self.pet.sleep()
        self.update_progress_bars()

    def exercise(self):
        self.pet.exercise()
        self.update_progress_bars()

    def update_progress_bars(self):
        self.root.ids.hunger_progress_bar.value = self.pet.hunger
        self.hunger_percentage = f"{self.pet.hunger}%"

        self.root.ids.happiness_progress_bar.value = self.pet.happiness
        self.happiness_percentage = f"{self.pet.happiness}%"

        self.root.ids.energy_progress_bar.value = self.pet.energy
        self.energy_percentage = f"{self.pet.energy}%"

class VirtualPet:
    def __init__(self):
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def feed(self):
        self.hunger = max(0, self.hunger - 10)
        self.happiness = min(100, self.happiness + 10)

    def play(self):
        self.happiness = min(100, self.happiness + 10)
        self.energy = max(0, self.energy - 10)

    def sleep(self):
        self.energy = min(100, self.energy + 10)
        self.hunger = min(100, self.hunger + 10)

    def exercise(self):
        self.happiness = max(0, self.happiness - 10)
        self.energy = max(0, self.energy - 10)


if __name__ == "__main__":
    VirtualPetApp().run()
                 