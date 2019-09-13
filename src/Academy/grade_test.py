from grade import Grade
from pytest import fixture
@fixture
def grade():
    attributes = (
        'Teologia',
        [],
        4,
        [{ 'name': 'Lucas Badico'}]
    )
    return Grade(attributes)

class TestGrade():
    def test_grade_has_subject(self, grade):
        assert grade.subject == 'Teologia'

    def test_grade_has_professors(self, grade):
        assert type(grade.professors) == list
    
    def test_grade_has_weekly_class(self, grade):
        assert grade.weekly_class == 4

    def test_grade_has_calculated_credits(self, grade):
        assert grade.credits == 30
    
    def test_grade_has_students(self, grade):
        assert type(grade.students) == list

    def test_grade_studentes_has_properties(self, grade):
        student = grade.students[0]
        assert student['name'] == 'Lucas Badico'
    
    def test_grade_has_student_score_avaliation(self, grade):
        student = grade.students[0]
        print('studant', student)
        assert student['approved'] == False