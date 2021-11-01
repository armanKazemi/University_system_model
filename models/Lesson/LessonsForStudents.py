from models.Lesson.Lesson import Lesson


class LessonForStudents(Lesson):
    """
    Model of LESSON for students. Use for passing a lecture.
    """

    def __init__(self):
        super().__init__()
        self._students_name_list = []  # students name list that have this lecture. (type of indexes: String)
        self._practices_list = []      # practices list of lecture. (type of indexes: String)
        self._teacher_assistants_name_list = []  # teacher assistants' name list. (type of indexes: String)
        self._grades_chart = {}        # dictionary of lecture's grades. (key: grade's name, value: grade)
        self._sources = ''             # lecture sources
        self._inside_exams_list = []   # list of inside exams. (type of indexes: String)
        self._student_grades = {}      # dictionary of student's grades. (key: grade's name, value: grade)
        self._final_student_grade = 0.0  # final student grade
        self._to_pass_status = ''      # to pass status [passed/in progress/removed]

    def get_students_name_list(self):
        return self._students_name_list

    def set_students_name_list(self, students_name_list):
        self._students_name_list = students_name_list

    def add_to_students_name_list(self, new_student_name):
        self._students_name_list.append(new_student_name)

    def remove_from_students_name_list(self, student_name):
        self._students_name_list.remove(student_name)

    def get_practices_list(self):
        return self._practices_list

    def set_practices_list(self, practices_list):
        self._practices_list = practices_list

    def add_to_practices_list(self, new_practice):
        self._practices_list.append(new_practice)

    def remove_from_practices_list(self, practice):
        self._practices_list.remove(practice)

    def get_teacher_assistants_name_list(self):
        return self._teacher_assistants_name_list

    def set_teacher_assistants_name_list(self, teacher_assistants_name_list):
        self._teacher_assistants_name_list = teacher_assistants_name_list

    def add_to_teacher_assistants_name_list(self, new_teacher_assistant_name):
        self._teacher_assistants_name_list.append(new_teacher_assistant_name)

    def remove_from_teacher_assistants_name_list(self, teacher_assistant_name):
        self._teacher_assistants_name_list.remove(teacher_assistant_name)

    def get_grades_chart(self):
        return self._grades_chart

    def set_grades_chart(self, grades_chart):
        self._grades_chart = grades_chart

    def add_to_grades_chart(self, new_grade):
        self._grades_chart.update(new_grade)

    def remove_from_grades_chart(self, grade_key):
        self._grades_chart.pop(grade_key, None)

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

    def get_student_grades(self):
        return self._student_grades

    def set_student_grades(self, student_grades):
        self._student_grades = student_grades

    def add_to_student_grades(self, new_grade):
        self._student_grades.update(new_grade)

    def remove_from_student_grades(self, grade_key):
        self._student_grades.pop(grade_key, None)

    def get_final_student_grade(self):
        return self._final_student_grade

    def set_final_student_grade(self, final_student_grade):
        self._final_student_grade = final_student_grade

    def get_to_pass_status(self):
        return self._to_pass_status

    def set_to_pass_status(self, to_pass_status):
        self._to_pass_status = to_pass_status

    def __str__(self):
        def iterate_list(li):
            message = ""
            for index, item in enumerate(li):
                message += f"\t{index + 1}. {item}\n"
            return message

        def iterate_dict(di):
            message = ""
            for key in di:
                message += f"\t{key}: {di.get(key)}\n"
            return message

        return super().__str__() + \
               f"\n" \
               f"More information:\n" \
               f"\tTeacher assistants name: \n" \
               f"{iterate_list(self._teacher_assistants_name_list)}\n" \
               f"\tSources: \n" \
               f"{iterate_list(self._sources)}\n" \
               f"\tInside exams: \n" \
               f"{iterate_list(self._inside_exams_list)}\n" \
               f"\tPractices :\n" \
               f"{iterate_list(self._practices_list)}\n" \
               f"\tGrades chart: \n" \
               f"{iterate_dict(self._grades_chart)}\n" \
               f"\tLesson students name: \n" \
               f"{iterate_list(self._students_name_list)}\n" \
               f"\tStudent grade: \n" \
               f"{iterate_dict(self._student_grades)}\n" \
               f"\tFinal student grade: {self._final_student_grade}\n" \
               f"\tTo pass status: {self._to_pass_status}\n"
