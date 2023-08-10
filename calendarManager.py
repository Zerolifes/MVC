# import library
from setting import *
from widget import Widget
from textview import Textview
from button import Button


class CalendarManager(Widget):
    def __init__(self, parent , pos = [0, 0], size = [0, 0], align = [Align.NONE, Align.NONE], background = WHITE, boderRadius = 0):
        super().__init__(parent=parent, pos=pos, size=size, align=align, background=background, boderRadius=boderRadius)
        # declare views

        # 1/ month and year
        month = Widget(parent=self, name="monthView", pos=[20, 20], size=[100,50])
        monthText = Textview(parent=month,  text="August 2023")
        month.views.append(monthText)
        self.month = month
        self.views.append(self.month)

        # 2/ tools: month and week
        tools = Widget(parent=self, name="toolsView", pos=[20,20], size=[70, self.month.h], align=[Align.CENTER, Align.NONE])
        # week button
        weekDiv = Widget(parent=tools, name="weekButton", pos=[0,0], size=[tools.w // 2, tools.h], hover=WHITE)
        weekButton = Button(parent=weekDiv, text="week", wrap=False)
        weekDiv.views.append(weekButton)
        tools.views.append(weekDiv)
        self.weekButton = weekDiv

        # month button
        monthDiv = Widget(parent=tools, pos=[tools.w // 2, 0], size=[tools.w // 2, tools.h], hover=WHITE)
        monthButton = Button(parent=monthDiv, text="month", wrap=False)
        monthDiv.views.append(monthButton)
        tools.views.append(monthDiv)
        self.monthButton = monthDiv

        self.views.append(tools)

    def draw(self, surface, type=User.NONE, infor="none"):
        self.update(type=type, infor=infor)
        super().draw(surface)

    def update(self, type=User.NONE, infor="none"):
        match type:
            case User.MOUSE:
                self.mouseListener(infor)
        super().update()

    def mouseListener(self, infor):
        pos = infor
        if checkin(pos, self.month):
            self.weekButton.background = "WHITE"
            changeView(self.views, "weekButton", self.weekButton)

