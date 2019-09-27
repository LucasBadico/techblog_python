from functools import reduce
from operator import add
class StudentCurricullum():
    def __init__(self, attributes):
        course_name, student, grades = attributes
        self.course_name = course_name
        self.grades = grades
        self.student = student
    
    @property
    def total_credits(self):
        extractCredit = lambda grade: grade.get('credits') or 0
        return reduce(add,  [extractCredit(grade) for grade in self.grades])

    @property
    def total_score(self):
        extractScore = lambda grade: grade.get('score') or 0
        return reduce(add,  [extractScore(grade) for grade in self.grades]) / len(self.grades)