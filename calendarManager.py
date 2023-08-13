# import library
import datetime
from setting import *
from widget import Widget
from textview import Textview
from button import Button
from calendarTable import CalendarTable


class CalendarManager(Widget):
    def __init__(self, parent , pos = [0, 0], size = [0, 0], align = [Align.NONE, Align.NONE], background = WHITE, boderRadius = 0):
        super().__init__(parent=parent, pos=pos, size=size, align=align, background=background, boderRadius=boderRadius)
        # declare views

        # 1/ month and year
        today = datetime.date.today()
        text = today.strftime("%B  %Y")
        self.month = Textview(parent=self, name="monthView", pos=[20, 20], wrap=False, text=text, align=[Align.NONE, Align.NONE])
        self.views.append(self.month)

        # 2/ tools: month and day
        self.tools = Widget(parent=self, name="toolsView", pos=[20,20], size=[80, self.month.h], align=[Align.CENTER, Align.NONE])
        # day button
        self.dayButtonDiv = Widget(parent=self.tools, name="dayButton", pos=[0,0], size=[self.tools.w // 2, self.tools.h], hover=WHITE)
        self.dayButton = Button(parent=self.dayButtonDiv, text="day", wrap=False)
        self.dayButtonDiv.views.append(self.dayButton)
        self.tools.views.append(self.dayButtonDiv)

        # month button
        self.monthButtonDiv = Widget(parent=self.tools, name="monthButton", pos=[self.tools.w // 2, 0], size=[self.tools.w // 2, self.tools.h], hover=WHITE, background=WHITE)
        self.monthButton = Button(parent=self.monthButtonDiv, text="month", wrap=False)
        self.monthButtonDiv.views.append(self.monthButton)
        self.tools.views.append(self.monthButtonDiv)

        self.views.append(self.tools)

        # 3/ today tools
        today = Widget(parent=self, pos=[640, self.month.y], size=[100, self.tools.h])
        # prev Button
        prevDiv = Widget(parent=today, pos=[0,0], size=[20, today.h], hover=WHITE)
        prevButton = Button(parent=prevDiv, wrap=False, text="<")
        prevDiv.views.append(prevButton)
        today.views.append(prevDiv)
        self.prevButton = prevDiv

        # today Button
        todayDiv = Widget(parent=today, pos=[20, 0], size=[40, today.h], hover=WHITE, align=[Align.CENTER, Align.NONE])
        todayButton = Button(parent=todayDiv, text="Today", wrap=False)
        todayDiv.views.append(todayButton)
        today.views.append(todayDiv)
        self.todayButton = todayDiv

        # next Button
        nextDiv = Widget(parent=today, pos=[80, 0], size=[prevDiv.w, today.h], hover=WHITE)
        nextButton = Button(parent=nextDiv, text=">", wrap=False)
        nextDiv.views.append(nextButton)
        today.views.append(nextDiv)
        self.nextButton = nextDiv

        self.views.append(today)
        self.todayTools = today

        # 4/ frame of calendar
        self.calendar = CalendarTable(parent=self)
        self.views.append(self.calendar)


        # 5/ date bar
        self.dateBar = Widget(parent=self, name="dateBar", pos=[self.calendar.x, 55], size=[self.calendar.w, 20], align=[Align.CENTER, Align.NONE])
        dates = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        for i in range(len(dates)):
            dayDiv = Widget(parent=self.dateBar, pos=[self.calendar.dayWidth * i, 0])
            dayText = Textview(parent=dayDiv, wrap=True, text=dates[i])
            dayDiv.views.append(dayText)
            self.dateBar.views.append(dayDiv)

        self.views.append(self.dateBar)


        # 6/ day note
        self.dayNote = Widget(parent = self, name="dayNote", pos=[0, self.calendar.y], size=[self.calendar.w, self.calendar.h], align=[Align.CENTER, Align.NONE], display=Display.HIDE, background=WHITE, boderRadius=10)
        self.views.append(self.dayNote)

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
        if checkin(pos, self.monthButtonDiv):
            self.monthButtonDiv.background = WHITE
            self.dayButtonDiv.background = SILVER
            self.calendar.display = Display.SHOW
            self.dayNote.display = Display.HIDE

        # click on day Button
        elif checkin(pos, self.dayButton):
            self.dayButtonDiv.background = WHITE
            self.monthButtonDiv.background = SILVER
            self.calendar.display = Display.HIDE
            self.dayNote.display = Display.SHOW

        # click on next Button
        elif checkin(pos, self.nextButton):
            self.calendar.nextMonth()
            self.month.text = self.calendar.inforDay

        # click on prev Button
        elif checkin(pos, self.prevButton):
            self.calendar.prevMonth()
            self.month.text = self.calendar.inforDay

        # click on today Button
        elif checkin(pos, self.todayButton):
            self.calendar.nowMonth()
            self.month.text = self.calendar.inforDay
