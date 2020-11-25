from functools import reduce
from operator import add
class ClassRoom():
    def __init__(self, attributes):
        course_name, identifier, calendar, students = attributes
        code, year, semester = identifier
        self.code = code
        self.year = year
        self.semester = semester
        self.course_name = course_name
        self.calendar = calendar
        self.students = students
        print('&&&&')
        print(calendar)
    
    @property
    def meetings(self):
        process_meetings = lambda date, self: {
            'date': date,
            'course_name': self.course_name,
            'students': self.students
        }
        return [process_meetings(date, self) for date in self.calendar]

    @property
    def total_score(self):
        extractScore = lambda grade: grade.get('score') or 0
        return ({course_name: self.course_name})