from models.Person.Employee import Employee


class Teacher(Employee):
    """
    Model of TEACHER specific information.
    """

    def __init__(self):
        super().__init__()
        self._dedicated_fields = []    # dedicated fields name. (type of indexes: String)
        self._is_supervisor = False    # is supervisor
        self._is_science_committee = False   # is member of science committee
        self._is_head_of_department = False  # is head of department
        self._lessons_list = []        # lessons list name for teaching. (type of indexes: LessonForTeachers)
        self._resume = None            # resume file. (type: File)

    def get_dedicated_fields(self):
        return self._dedicated_fields

    def set_dedicated_fields(self, dedicated_fields):
        self._dedicated_fields = dedicated_fields

    def is_supervisor(self):
        return self._is_supervisor

    def set_supervisor_status(self, supervisor_status):
        self._is_supervisor = supervisor_status

    def is_science_committee(self):
        return self._is_science_committee

    def set_science_committee_status(self, science_committee_status):
        self._is_science_committee = science_committee_status

    def is_head_of_department(self):
        return self._is_head_of_department

    def set_head_of_department_status(self, head_of_department_status):
        self._is_head_of_department = head_of_department_status

    def get_lessons_list(self):
        return self._lessons_list

    def set_lessons_list(self, lessons_list):
        self._lessons_list = lessons_list

    def add_to_lessons_list(self, new_lesson):
        self._lessons_list.append(new_lesson)

    def remove_from_lessons_list(self, lesson):
        self._lessons_list.remove(lesson)

    def get_resume(self):
        return self._resume

    def set_resume(self, resume):
        self._resume = resume

    def __str__(self):
        def iterate_list(list_name, li):
            message = ""
            for index, item in enumerate(li):
                if list_name == '':
                    message += f"\t{index+1}. {item}\n"
                else:
                    message += f"\t{list_name} {index + 1}\n" \
                               f" {item}\n"
            return message
        return super().__str__() + \
               f"\n" \
               f"Teacher's Information:\n" \
               f"\tDedicated fields: {iterate_list('', self._dedicated_fields)}\n" \
               f"\tIs supervisor? {'Yes' if self._is_supervisor else 'No'}\n" \
               f"\tIs head of department? {'Yes' if self._is_head_of_department else 'No'}\n" \
               f"\tIs science committee? {'Yes' if self._is_science_committee else 'No'}\n" \
               f"\tLessons list: {iterate_list('Lesson', self._lessons_list)}\n"
