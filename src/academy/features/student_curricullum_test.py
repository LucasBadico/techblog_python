from student_curricullum import StudentCurricullum
from pytest import fixture

@fixture
def curricullum():
    student = { 'name': 'Lucas Badico' }
    grades = [{
        'subject': 'grego',
        'score': 10,
        'credits': 5,
    },
    {
        'subject': 'grego',
        'score': 10,
        'credits': 10,
    },
    {
        'subject': 'grego',
        'score': 10,
    }]
    curricullum = StudentCurricullum(('Master of Ministry', student, grades))
    return curricullum

class TestStudentCurricullum():
    def test_curricullum_has_course_name(self, curricullum):
        assert curricullum.course_name == 'Master of Ministry'

    def test_curricullum_has_student_properties(self, curricullum):
        assert curricullum.student['name'] == 'Lucas Badico'

    def test_curricullum_has_calculated_total_credits(self, curricullum):
        assert curricullum.total_credits == 15

    def test_curricullum_has_grades_is_list(self, curricullum):
        assert type(curricullum.grades) == list

    def test_curricullum_grades_item_has_properties(self, curricullum):
        grade = curricullum.grades[0]
        assert grade['subject'] == 'grego'
        assert grade['credits'] == 5
        assert grade['score'] == 10

    def test_curricullum_has_calculeted_total_score(self, curricullum):
        assert curricullum.total_score == 10
        