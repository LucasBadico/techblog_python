from grade import Grade
from student_curricullum import StudentCurricullum
from grade_test import grade
from student_curricullum_test import curricullum
class TestMain:
    def test_student_curricullum_integrated_with_grade(self, grade):
        student = { 'name': 'Lucas Badico' }
        grades = [ grade ]
        curricullum = StudentCurricullum(('Master of Ministry', student, grades))
        assert False