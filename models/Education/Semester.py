class Semester:
    """
    Model of SEMESTER, student's semester's information.
    """

    def __init__(self):
        self._semester_code = '0000'  # semester code
        self._lessons_list_for_student = []  # student list of lectures (type of indexes: Lesson)
        self._is_probation = False    # probation status
        self._semester_average = 0.0  # semester average
        self._number_of_units = 12    # semester number of units
        self._number_of_removed_units = 0  # semester number of removed units

    def get_semester_code(self):
        return self._semester_code

    def set_semester_code(self, semester_code):
        self._semester_code = semester_code

    def get_lessons_list_for_student(self):
        return self._lessons_list_for_student

    def set_lessons_list_for_student(self, lessons_list_for_student):
        self._lessons_list_for_student = lessons_list_for_student

    def add_to_lessons_list_for_student(self, new_lesson):
        self._lessons_list_for_student.append(new_lesson)

    def remove_from_lessons_list_for_student(self, lesson):
        self._lessons_list_for_student.remove(lesson)

    def is_probation(self):
        return self._is_probation

    def set_probation_status(self, probation_status):
        self._is_probation = probation_status

    def get_semester_average(self):
        return self._semester_average

    def set_semester_average(self, semester_average):
        self._semester_average = semester_average

    def get_number_of_units(self):
        return self._number_of_units

    def set_number_of_units(self, number_of_units):
        self._number_of_units = number_of_units

    def get_number_of_removed_units(self):
        return self._number_of_removed_units

    def set_number_of_removed_units(self, number_of_removed_units):
        self._number_of_removed_units = number_of_removed_units

    def __str__(self):
        def iterate_list(list_name, li):
            message = ""
            for index, item in enumerate(li):
                message += f"\t{list_name} {index + 1}:\n" \
                           f"{item}\n"
            return message

        return f"\tSemester code: {self._semester_code}\n" \
               f"\tProbation status: " + "Probation" if self._is_probation else "-" + "\n" + \
               f"\tSemester average: {self._semester_average}\n" \
               f"\tNumber of semester units: {self._number_of_units}\n" \
               f"\tNumber of semester removed units: {self._number_of_removed_units}\n" \
               f"\tLessons list of semester: \n" + iterate_list('Lesson', self._lessons_list_for_student) + "\n"
