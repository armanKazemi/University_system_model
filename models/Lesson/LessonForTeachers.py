from models.Lesson.Lesson import Lesson


class LessonForTeachers(Lesson):
    """
    Model of LESSON for teachers. Use for teaching and communicate with students.
    """

    def __init__(self):
        super().__init__()
        self._students_list = []   # students list that have this lecture. (type of indexes: Student)
        self._practices_list = []  # practices list of lecture. (type of indexes: String)
        self._teacher_assistants_list = []  # teacher assistants list. (type of indexes: Student)
        self._grades_chart = {}    # dictionary of lecture grades. (key: grade's name, value: grade)
        self._sources = ''         # lecture sources
        self._inside_exams_list = []  # list of inside exams. (type of indexes: String)

    def get_students_name_list(self):
        return self._students_list

    def set_students_list(self, students_list):
        self._students_list = students_list

    def add_to_students_name_list(self, new_student):
        self._students_list.append(new_student)

    def remove_from_students_name_list(self, student):
        self._students_list.remove(student)

    def get_practices_list(self):
        return self._practices_list

    def set_practices_list(self, practices_list):
        self._practices_list = practices_list

    def add_to_practices_list(self, new_practice):
        self._practices_list.append(new_practice)

    def remove_from_practices_list(self, practice):
        self._practices_list.remove(practice)

    def get_teacher_assistants_list(self):
        return self._teacher_assistants_list

    def set_teacher_assistants_list(self, teacher_assistants_list):
        self._teacher_assistants_list = teacher_assistants_list

    def add_to_teacher_assistants_list(self, new_teacher_assistant):
        self._teacher_assistants_list.append(new_teacher_assistant)

    def remove_from_teacher_assistants_list(self, teacher_assistant):
        self._teacher_assistants_list.remove(teacher_assistant)

    def get_grades_chart(self):
        return self._grades_chart

    def set_grades_chart(self, grades_chart):
        self._grades_chart = grades_chart

    def add_to_grades_chart(self, new_grade):
        self._grades_chart.update(new_grade)

    def remove_from_grades_chart(self, grade):
        self._grades_chart.pop(list(grade.keys())[0], None)

    def get_sources(self):
        return self._sources

    def set_sources(self, sources):
        self._sources = sources

    def get_inside_exams_list(self):
        return self._inside_exams_list

    def set_inside_exams_list(self, inside_exams_list):
        self._inside_exams_list = inside_exams_list

    def add_to_inside_exams_list(self, new_inside_exam):
        self._inside_exams_list.append(new_inside_exam)

    def remove_from_inside_exams_list(self, inside_exam):
        self._inside_exams_list.remove(inside_exam)

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

        def iterate_dict(di):
            message = ""
            for key in di:
                message += f"\t{key}: {di.get(key)}\n"
            return message

        return super().__str__() + \
               f"\n" \
               f"More information:\n" \
               f"\tStudents: \n" \
               f"{iterate_list('Student', self._students_list)}\n"\
               f"\tTeacher assistants: \n" \
               f"{iterate_list('Teacher assistant', self._teacher_assistants_list)}\n" \
               f"\tSources: \n" \
               f"{iterate_list('', self._sources)}\n" \
               f"\tInside exams: \n" \
               f"{iterate_list('', self._inside_exams_list)}\n" \
               f"\tPractices :\n" \
               f"{iterate_list('', self._practices_list)}\n" \
               f"\tGrades chart: \n" \
               f"{iterate_dict(self._grades_chart)}\n" \
