import pandas as pd
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

class CharacterInfo(App,GridLayout,ButtonBehavior):
    def __init__(self):
        super(CharacterInfo, self).__init__()
        self.cols = 2
        self.characters = pd.read_csv("items.csv")
        self.imgSource = []
        self.charNames = []
        self.charBdays = []
        self.charGift = []
        self.rowCount = 0
        self.popup = Popup(title="Character View")
        for x,y in self.characters.iterrows():
            self.imgSource.append(str(self.characters.iloc[self.rowCount]["File"]))
            self.charNames.append(str(self.characters.iloc[self.rowCount]["Name"]))
            self.charBdays.append(str(self.characters.iloc[self.rowCount]["Birthday"]))
            self.charGift.append(str(self.characters.iloc[self.rowCount]["Gift"]))
            self.add_widget(Image(source=self.characters.iloc[self.rowCount]["File"]))
            self.charButton = Button(text=self.characters.iloc[self.rowCount]["Name"], on_press=self.pressed)
            self.charButton.name = self.rowCount
            self.add_widget(self.charButton)
            self.rowCount = self.rowCount + 1

    
    def pressed(self, instance):
        layout = GridLayout(cols=1)
        infoName = str(instance.text)
        infoIndex = self.charNames.index(infoName)
        name = Label(text=self.charNames[infoIndex])
        image = Image(source=self.imgSource[infoIndex])
        bday = Label(text="Birthday: " + self.charBdays[infoIndex])
        gift = Label(text="Favourite Gift: " + self.charGift[infoIndex])
        closeButton = Button(text="Back")
        layout.add_widget(name)
        layout.add_widget(image)
        layout.add_widget(bday)
        layout.add_widget(gift)
        layout.add_widget(closeButton)
        self.popup = Popup(
            title="Character Profile", 
            content=layout, auto_dismiss=False,
            size_hint=(None,None), size=(800,800)
        )
        self.popup.open()
        closeButton.bind(on_press=self.on_close)

    def on_close(self, event):
        print('here')
        self.popup.dismiss()

    def build(self):
        return CharacterInfo()
     
  