from copy import deepcopy
class ClassRoom():
    def __init__(self, attributes):
        subject, professors, weekly_class, students = attributes
        self.subject = subject
        self.weekly_class = weekly_class
        self.professors = professors
        self._students = students
    
    @property
    def credits(self):
        weekly_class_to_credits_factor = 2
        units_of_credit = self.weekly_class/weekly_class_to_credits_factor
        value_of_credit = 15
        return int(units_of_credit * value_of_credit)
    
    @property
    def students(self):
        return list(map(self.proccess_approval, self._students))

    def proccess_approval(self, student):
        approved = False
        if student.get('score') and student.score >= 7:
            approved = True
        
        studentWithApprovedProperty = deepcopy(student)
        studentWithApprovedProperty['approved'] = approved
        return studentWithApprovedProperty