# import library
import datetime
from setting import *
from widget import Widget
from textview import Textview
from button import Button
from calendarTable import CalendarTable
from dayNote import DayNote


class CalendarManager(Widget):
    def __init__(self, parent , pos = [0, 0], size = [0, 0], align = [Align.NONE, Align.NONE], background = WHITE, boderRadius = 0):
        super().__init__(parent=parent, pos=pos, size=size, align=align, background=background, boderRadius=boderRadius)
        # declare views

        # 1/ month and year
        self.now = datetime.date.today()
        text = self.now.strftime("%B %Y")
        self.month = Textview(parent=self, name="monthView", pos=[20, 20], wrap=False, text=text, align=[Align.NONE, Align.NONE])
        self.views.append(self.month)

        # 2/ tools: month and day
        self.tools = Widget(parent=self, name="toolsView", pos=[20,20], size=[80, self.month.h], align=[Align.CENTER, Align.NONE])
        # day button
        self.dayButtonDiv = Widget(parent=self.tools, name="dayButton", pos=[0,0], size=[self.tools.w // 2, self.tools.h])
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
        self.todayTools = Widget(parent=self, pos=[640, self.month.y], size=[100, self.tools.h])
        # prev Button

        self.prevButtonDiv = Widget(parent=self.todayTools, pos=[0,0], size=[20, self.todayTools.h], hover=WHITE)
        self.prevButton = Button(parent=self.prevButtonDiv, wrap=False, text="<")
        self.prevButtonDiv.views.append(self.prevButton)
        self.todayTools.views.append(self.prevButtonDiv)

        # today Button
        self.todayButtonDiv = Widget(parent=self.todayTools, pos=[20, 0], size=[40, self.todayTools.h], hover=WHITE, align=[Align.CENTER, Align.NONE])
        self.todayButton = Button(parent=self.todayButtonDiv, text="Today", wrap=False)
        self.todayButtonDiv.views.append(self.todayButton)
        self.todayTools.views.append(self.todayButtonDiv)

        # next Button
        self.nextButtonDiv = Widget(parent=self.todayTools, pos=[80, 0], size=[self.prevButtonDiv.w, self.todayTools.h], hover=WHITE)
        self.nextButton = Button(parent=self.nextButtonDiv, text=">", wrap=False)
        self.nextButtonDiv.views.append(self.nextButton)
        self.todayTools.views.append(self.nextButtonDiv)

        self.views.append(self.todayTools)

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
        self.dayNote = DayNote(parent=self)
        self.views.append(self.dayNote)

    def draw(self, surface, userContact=User.NONE, infor="none"):
        self.update(userContact=userContact, infor=infor)
        super().draw(surface)

    def update(self, userContact=User.NONE, infor="none"):
        match userContact:
            case User.MOUSE:
                self.mouseListener(infor)
            case User.KEYBOARD:
                self.keyboardListener(infor)
        super().update()

    def mouseListener(self, infor):
        pos = infor

        # click on month Button
        if checkin(pos, self.monthButtonDiv):
            self.monthButtonDiv.background = WHITE
            self.dayButtonDiv.background = SILVER
            self.calendar.display = Display.SHOW
            self.dayNote.display = Display.HIDE
            self.todayTools.display = Display.SHOW
            self.dateBar.display = Display.SHOW
            self.month.text = self.calendar.dateDisplay.strftime('%B %Y')

        # click on next Button
        elif checkin(pos, self.nextButtonDiv):
            self.calendar.nextMonth()
            self.month.text = self.calendar.inforDay

        # click on prev Button
        elif checkin(pos, self.prevButtonDiv):
            self.calendar.prevMonth()
            self.month.text = self.calendar.inforDay

        # click on today Button
        elif checkin(pos, self.todayButtonDiv):
            self.calendar.nowMonth()
            self.month.text = self.calendar.inforDay

        # choose day of month
        elif checkin(pos, self.calendar) and self.calendar.display == Display.SHOW:
            if not self.calendar.mouseListener(pos): return
            self.dayButtonDiv.background = WHITE
            self.monthButtonDiv.background = SILVER
            self.calendar.display = Display.HIDE
            self.dayNote.display = Display.SHOW
            self.todayTools.display = Display.HIDE
            self.dateBar.display = Display.HIDE
            self.month.text = self.calendar.dateDisplay.strftime("%B %d, %Y")
            self.dayNote.hide()
            self.dayNote.show()

        
        # click on add Button
        elif checkin(pos, self.dayNote.addButtonDiv) and self.dayNote.display == Display.SHOW:
            self.dayNote.typing = True
            self.dayNote.note[self.dayNote.noteCurent].text = "_"

        # click delete Button
        elif checkin(pos, self.dayNote.deleteButtonDiv) and self.dayNote.display == Display.SHOW:
            database = open("data.txt", "r")
            datas = database.read().split('|||')
            database.close()
            database = open("data.txt", 'w')
            for data in datas:
                if data == "": break
                content = data.split('///')
                print(content)
                if content[0] != self.month.text:
                    database.write(content[0]+"///"+content[1]+"|||")
            self.dayNote.hide()
            self.dayNote.show()
            

    def keyboardListener(self, infor):
        self.dayNote.keyboardListener(infor)


