# import library
import datetime
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
        today = datetime.date.today()
        text = today.strftime("%B  %Y")
        monthText = Textview(parent=month,  text=text)
        month.views.append(monthText)
        self.views.append(month)
        self.month = month

        # 2/ tools: month and day
        tools = Widget(parent=self, name="toolsView", pos=[20,20], size=[80, self.month.h], align=[Align.CENTER, Align.NONE])
        # day button
        dayDiv = Widget(parent=tools, name="dayButton", pos=[0,0], size=[tools.w // 2, tools.h], hover=WHITE)
        dayButton = Button(parent=dayDiv, text="day", wrap=False)
        dayDiv.views.append(dayButton)
        tools.views.append(dayDiv)
        self.dayButton = dayDiv

        # month button
        monthDiv = Widget(parent=tools, name="monthButton", pos=[tools.w // 2, 0], size=[tools.w // 2, tools.h], hover=WHITE, background=WHITE)
        monthButton = Button(parent=monthDiv, text="month", wrap=False)
        monthDiv.views.append(monthButton)
        tools.views.append(monthDiv)
        self.monthButton = monthDiv
        self.views.append(tools)
        self.tools = tools

        # 3/ today
        today = Widget(parent=self, pos=[640, self.month.y], size=[100, self.tools.h])
        # prev Button
        prevDiv = Widget(parent=today, pos=[0,0], size=[20, today.h], hover=WHITE)
        prevButton = Button(parent=prevDiv, wrap=False, text="<")
        prevDiv.views.append(prevButton)
        today.views.append(prevDiv)

        # today Button
        todayDiv = Widget(parent=today, pos=[20, 0], size=[40, today.h], hover=WHITE, align=[Align.CENTER, Align.NONE])
        todayButton = Button(parent=todayDiv, text="Today", wrap=False)
        todayDiv.views.append(todayButton)
        today.views.append(todayDiv)

        # next Button
        nextDiv = Widget(parent=today, pos=[80, 0], size=[prevDiv.w, today.h], hover=WHITE)
        nextButton = Button(parent=nextDiv, text=">", wrap=False)
        nextDiv.views.append(nextButton)
        today.views.append(nextDiv)

        self.views.append(today)
        self.today = today


        # 4/ frame of calendar
        calendar = Widget(parent=self,name="calendar", pos=[20, 80], size=[720, 450], align=[Align.CENTER, Align.NONE], background=WHITE)
        dayWidth = 103
        dayHeight = 90
        day = int(datetime.date.today().strftime("%d"))
        date = DATES[(datetime.date.today().strftime("%A"))]
        month = (datetime.date.today().strftime("%b"))
        dateEmpty = (7 - (day - date) % 7) % 7
        dateCount = 1
        dateLimit = dateEmpty + MONTHS[month]
        for i in range(5):
            for j in range(7):
                dayDiv = Widget(parent=calendar, pos=[dayWidth*j, dayHeight*i], size=[dayWidth, dayHeight], hover=WHITE)
                text = ""
                color = SILVER
                if dateEmpty < dateCount and dateCount <= dateLimit:
                    text = str(dateCount - dateEmpty)
                    color = GRAY
                dayWidget = Widget(parent=dayDiv, size=[dayWidth - 2, dayHeight - 2], background=color, align=[Align.CENTER, Align.CENTER], hover=WHITE)
                dateCount = dateCount + 1
                # daythDiv = Widget(parent=dayWidget, pos=[5,5])
                dayth = Textview(parent=dayWidget, text=text, wrap=False, align=[Align.NONE, Align.NONE], pos=[5,5])
                # daythDiv.views.append(dayth)
                dayWidget.views.append(dayth)
                dayDiv.views.append(dayWidget)
                calendar.views.append(dayDiv)

        self.views.append(calendar)
        self.calendar = calendar

        # 5/ date bar
        dateBar = Widget(parent=self, name="dateBar", pos=[calendar.x, 55], size=[calendar.w, 20], align=[Align.CENTER, Align.NONE])
        dates = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        for i in range(len(dates)):
            dayDiv = Widget(parent=dateBar, pos=[dayWidth*i, 0])
            dayText = Textview(parent=dayDiv, wrap=True, text=dates[i])
            dayDiv.views.append(dayText)
            dateBar.views.append(dayDiv)

        self.views.append(dateBar)
        self.dateBar = dateBar

        # 6/ day note
        dayNote = Widget(parent = self, name="dayNote", pos=[0, self.calendar.y], size=[self.calendar.w, self.calendar.h], align=[Align.CENTER, Align.NONE], display=Display.HIDE, background=WHITE, boderRadius=10)
        self.views.append(dayNote)
        self.dayNote = dayNote

    def draw(self, surface, userContact=User.NONE, infor="none"):
        self.update(userContact=userContact, infor=infor)
        super().draw(surface)

    def update(self, userContact=User.NONE, infor="none"):
        match userContact:
            case User.MOUSE:
                self.mouseListener(infor)
        super().update()

    def mouseListener(self, infor):
        pos = infor

        # click on month Button
        if checkin(pos, self.monthButton):
            self.monthButton.background = WHITE
            self.changeView("monthButton", self.monthButton)
            self.dayButton.background = SILVER
            self.changeView("dayButton", self.dayButton)
            self.calendar.display = Display.SHOW
            self.changeView("calendar", self.calendar)
            self.dateBar.display = Display.SHOW
            self.changeView("dateBar", self.dateBar)
            self.dayNote.display = Display.HIDE
            self.changeView("dayNote", self.dayNote)

        # click on day Button
        elif checkin(pos, self.dayButton):
            self.dayButton.background = WHITE
            self.changeView("dayButton", self.dayButton)
            self.monthButton.background = SILVER
            self.changeView("monthButton", self.monthButton)
            self.calendar.display = Display.HIDE
            self.changeView("calendar", self.calendar)
            self.dateBar.display = Display.HIDE
            self.changeView("dateBar", self.dateBar)
            self.dayNote.display = Display.SHOW
            self.changeView("dayNote", self.dayNote)

