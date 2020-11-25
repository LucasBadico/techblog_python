from class_room import ClassRoom
from pytest import fixture

@fixture
def class_room():
    identifier = ('mockcode', 2019, 1)
    # month, day, periodo(morning, evening, night), half one or half two
    calendar = (10,5,'morning', 1),
    students = { 'name': 'Amanda Varges'},
    class_room = ClassRoom(('Master of Ministry', identifier, calendar, students))
    return class_room

class TestClassRoom():
    def test_class_room_has_defined_attributes(self, class_room):
        assert class_room.course_name == 'Master of Ministry'
        assert class_room.year == 2019
        assert class_room.semester == 1
        assert class_room.code == 'mockcode'

    def test_class_room_can_return_classes(self, class_room):
        given_class, = class_room.meetings
        assert given_class.get('course_name') == 'Master of Ministry'
    
    def test_class_room_meetings_has_year_month_day(self, class_room):
        given_class, = class_room.meetings
        assert given_class.get('date') == (10,5,'morning', 1)
    
    def test_class_room_meetings_has_students(self, class_room):
        given_class, = class_room.meetings
        assert given_class.get('students') == ({ 'name': 'Amanda Varges'},)

    # def test_curricullum_has_calculated_total_credits(self, curricullum):
    #     assert curricullum.total_credits == 15

    # def test_curricullum_has_grades_is_list(self, curricullum):
    #     assert type(curricullum.grades) == list

    # def test_curricullum_grades_item_has_properties(self, curricullum):
    #     grade = curricullum.grades[0]
    #     assert grade['subject'] == 'grego'
    #     assert grade['credits'] == 5
    #     assert grade['score'] == 10

    # def test_curricullum_has_calculeted_total_score(self, curricullum):
    #     assert curricullum.total_score == 10
        