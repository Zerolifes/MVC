# import library
import datetime
from setting import *
from widget import Widget
from textview import Textview
from button import Button

class DayNote(Widget):
    def __init__(self,parent):
        super().__init__(parent = parent, pos=[0, parent.calendar.y], size=[parent.calendar.w, parent.calendar.h], align=[Align.CENTER, Align.NONE], display=Display.HIDE, background=WHITE, boderRadius=10)
        
        self.addButtonDiv = Widget(parent=self, pos=[650, 380], size=[40, 40], background=SILVER, hover=GRAY, boderRadius=40)
        addButton = Button(parent=self.addButtonDiv, wrap=False, text="+", fontSize=25)
        self.addButtonDiv.views.append(addButton)
        self.views.append(self.addButtonDiv)

        self.deleteButtonDiv = Widget(parent=self, pos=[550, 380], size=[60, 40], background=SILVER, hover=GRAY)
        deleteButton = Button(parent=self.deleteButtonDiv, wrap=False, text="x", fontSize=25)
        self.deleteButtonDiv.views.append(deleteButton)
        self.views.append(self.deleteButtonDiv)
        
        self.fontSize = 20
        self.typing = False
        self.text = ""
        self.noteCurent = 0
        self.note = [Textview(parent=self, pos=[20, 30 * self.noteCurent + 20], wrap=False, align=[Align.NONE, Align.NONE], fontSize=self.fontSize, text="")]

    def keyboardListener(self, infor):
        if not self.typing: return
        # pressed enter
        if infor == 13:
            self.typing = False
            self.updateData(self.text)
            self.noteCurent = self.noteCurent + 1
            self.note.append(Textview(parent=self, pos=[20, 30 * self.noteCurent + 20], wrap=False, align=[Align.NONE, Align.NONE], fontSize=self.fontSize, text=""))
            self.text = ""
            return
        # pressed backspace
        if infor == 8: self.text = self.text[:-1]
        else: self.text = self.text + chr(infor)
        self.note[self.noteCurent].text = self.text
        self.note[self.noteCurent].text = self.text + "_"

    def draw(self, surface):
        if (self.display == Display.HIDE): return
        super().draw(surface)
        for view in self.note:
            view.draw(surface)

    def getData(self):
        database = open("data.txt", "r")
        datas = database.read().split("|||")
        for data in datas:
            content = data.split("///")
            if  content[0] == self.parent.month.text:
                self.note.append(Textview(parent=self, pos=[20, 30 * self.noteCurent + 20], wrap=False, align=[Align.NONE, Align.NONE], fontSize=self.fontSize, text=content[1]))
                self.noteCurent = self.noteCurent + 1
        self.note.append(Textview(parent=self, pos=[20, 30 * self.noteCurent + 20], wrap=False, align=[Align.NONE, Align.NONE], fontSize=self.fontSize, text=""))
        database.close()

    def updateData(self, text):
        database = open("data.txt", "a")
        database.write(self.parent.month.text+"///"+text+"|||")
        database.close()

    def hide(self):
        self.text = ""
        self.noteCurent = 0
        self.note = []

    def show(self):
        self.getData()