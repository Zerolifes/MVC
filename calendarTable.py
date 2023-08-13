# import library
import datetime
from setting import *
from widget import Widget
from textview import Textview
from button import Button

class CalendarTable(Widget):
    def __init__(self, parent = "none"):
        super().__init__(parent=parent,name="calendar", pos=[20, 80], size=[720, 450], align=[Align.CENTER, Align.NONE], background=WHITE)
        self.dayWidth = 103
        self.dayHeight = 75
        self.dateCurrent = datetime.date.today()
        self.dateDisplay = self.dateCurrent
        self.crateMonth()

    def crateMonth(self):
        self.views = []
        self.inforDay = self.dateDisplay.strftime("%B  %Y")
        self.day = int(self.dateDisplay.strftime("%d"))
        self.date = DATES[(self.dateDisplay.strftime("%A"))]
        self.month = str(self.dateDisplay.strftime("%b"))
        self.year = int(self.dateDisplay.strftime("%Y"))
        self.daysofMonth = MONTHS[self.month]
        if self.month == "Feb" and self.year % 4 == 0: self.daysofMonth = self.daysofMonth + 1
        dateEmpty = (7 - (self.day - self.date) % 7) % 7
        dateCount = 1
        dateLimit = dateEmpty + self.daysofMonth
        for i in range(6):
            for j in range(7):
                dayDiv = Widget(parent=self, pos=[self.dayWidth*j, self.dayHeight*i], size=[self.dayWidth, self.dayHeight], hover=WHITE)
                text = ""
                color = SILVER
                if dateEmpty < dateCount and dateCount <= dateLimit:
                    text = str(dateCount - dateEmpty)
                    color = GRAY
                dayWidget = Widget(parent=dayDiv, size=[self.dayWidth - 2, self.dayHeight - 2], background=color, align=[Align.CENTER, Align.CENTER], hover=WHITE)
                dateCount = dateCount + 1
                # daythDiv = Widget(parent=dayWidget, pos=[5,5])
                dayth = Textview(parent=dayWidget, text=text, wrap=False, align=[Align.NONE, Align.NONE], pos=[5,5])
                # daythDiv.views.append(dayth)
                dayWidget.views.append(dayth)
                dayDiv.views.append(dayWidget)
                self.views.append(dayDiv)

    def nextMonth(self):
        self.dateDisplay = self.dateDisplay + datetime.timedelta(days=self.daysofMonth)
        self.crateMonth()

    def prevMonth(self):
        self.dateDisplay = self.dateDisplay - datetime.timedelta(days=self.daysofMonth)
        self.crateMonth()

    def nowMonth(self):
        self.dateDisplay = self.dateCurrent
        self.crateMonth()