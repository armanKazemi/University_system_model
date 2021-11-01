from models.Person.UniversityUser import UniversityUser


class Student(UniversityUser):
    """
    Model of STUDENT specific information.
    """

    _students_code_begin = 2000

    @classmethod
    def get_student_code_begin(cls):
        cls._students_code_begin += 1
        return cls._students_code_begin

    def __init__(self):
        super().__init__()
        self._student_code = '00000000'  # student number
        self._current_semester_number = 1  # current semester number
        self._supervisor = ''            # supervisor name
        self._total_average = 0          # total average till current semester
        self._field = ''                 # field name
        self._section_and_course = {}    # (key:section/course, value:value of them)
        self._semesters_list = []        # past semesters list. (type of indexes: Semester)
        self._total_units_number = 0     # total units number of semesters passed + units of current semester
        self._number_of_units_for_graduation_interval = {}  # total units number for graduation, 'based on field'
        self._current_semester = None    # current semester. (type: Semester)
        self._has_dormitory = False      # has dormitory or not
        self._tuition = 0                # amount of tuition

    def get_student_code(self):
        return self._student_code

    def set_student_code(self, student_code):
        self._student_code = student_code

    def get_current_semester_num(self):
        return self._current_semester_number

    def set_current_semester_num(self, current_semester_num):
        self._current_semester_number = current_semester_num

    def get_supervisor_name(self):
        return self._supervisor

    def set_supervisor_name(self, supervisor_name):
        self._supervisor = supervisor_name.capitalize().strip()

    def get_total_average(self):
        return self._total_average

    def set_total_average(self, total_average):
        self._total_average = total_average

    def get_field(self):
        return self._field

    def set_field(self, field):
        self._field = field.capitalize().strip()

    def get_section_and_course(self):
        return self._section_and_course

    def set_section_and_course(self, section, course):
        self._section_and_course['section'] = section.capitalize().strip()
        self._section_and_course['course'] = course.capitalize().strip()

    def get_semesters_list(self):
        return self._semesters_list

    def set_semesters_list(self, semesters_list):
        self._semesters_list = semesters_list

    def add_to_semesters_list(self, new_semester):
        self._semesters_list.append(new_semester)

    def remove_from_semesters_list(self, semester):
        self._semesters_list.remove(semester)

    def get_total_units_number(self):
        return self._total_units_number

    def set_total_units_number(self, total_units_number):
        self._total_units_number = total_units_number

    def get_number_of_units_for_graduation_interval(self):
        return self._number_of_units_for_graduation_interval

    def set_number_of_units_for_graduation_interval(self, begin, end):
        self._number_of_units_for_graduation_interval['begin'] = begin
        self._number_of_units_for_graduation_interval['end'] = end

    def get_current_semester(self):
        return self._current_semester

    def set_current_semester(self, current_semester):
        self._current_semester = current_semester

    def has_dormitory(self):
        return self._has_dormitory

    def set_dormitory_status(self, dormitory_status):
        self._has_dormitory = dormitory_status

    def get_tuition(self):
        return self._tuition

    def set_tuition(self, tuition):
        self._tuition = tuition

    def __str__(self):
        def iterate_list(list_name, li):
            message = ""
            for index, item in enumerate(li):
                message += f"\t{list_name} {index + 1}:\n"
                message += f"{item}\n"
            return message

        return super().__str__() + \
               f"\tRole in university: Student\n" \
               f"\n" \
               f"Student's Information:\n" \
               f"\tStudent code: {self._student_code}\n" \
               f"\tField: {self._field}\n" \
               f"\tSection and Course: {self._section_and_course}\n" \
               f"\tSupervisor: {self._supervisor}\n" \
               f"\tCurrent semester number: {self._current_semester}\n" \
               f"\tCurrent semester: {self._current_semester}\n" \
               f"\tPast semesters list:\n" + iterate_list('Semester', self._semesters_list) + \
               f"\tNumber of units for graduation: " \
               f"[{self._number_of_units_for_graduation_interval.get('begin')}, " \
               f"{self._number_of_units_for_graduation_interval.get('end')}]\n" \
               f"\tTotal number of student's units: {self._total_units_number}\n" \
               f"\tTotal average: {self._total_average}\n" \
               f"\tHas dormitory? " + "Yes" if self._has_dormitory else "No" + "\n" \
               f"\tTuition: {self._tuition} Rial"
