class Lesson:
    """
    Model of LESSON. Use for presenting lessons for students to choose
    """

    def __init__(self):
        self._lesson_type = ''        # lecture type [specialized / general]
        self._lesson_type_in_its_field = ''  # lecture type [necessary/selective/optional]
        self._lesson_name = ''        # lecture name
        self._lesson_code = ''        # lecture code
        self._teacher_of_lesson = ''  # teacher name
        self._class_schedule = []     # times of holding class, weekday and clock. (type of indexes: Time)
        self._location = {}           # location of class of lecture
        self._exam_info = {}          # exam info, location, date and clock. (key:'location'/'time', value:dict/Time)
        self._number_of_total_units = 0        # lesson number of total units
        self._number_of_theoretical_units = 0  # lesson number of theoretical units
        self._number_of_practical_units = 0    # lesson number of practical units
        self._education_group = ''    # education group name that present lecture
        self._field_name = ''         # field name that present lecture
        self._allowed_fields = []     # fields name that allowed to choosing. (type of indexes: String)
        self._tuition = 0.0           # lecture tuition for Tuition Student / removed lesson

    def get_lesson_type(self):
        return self._lesson_type

    def set_lesson_type(self, lesson_type):
        self._lesson_type = lesson_type

    def get_lesson_type_in_its_field(self):
        return self._lesson_type_in_its_field

    def set_lesson_type_in_its_field(self, lesson_type_in_its_field):
        self._lesson_type_in_its_field = lesson_type_in_its_field

    def get_lesson_name(self):
        return self._lesson_name

    def set_lesson_name(self, lesson_name):
        self._lesson_name = lesson_name

    def get_lesson_code(self):
        return self._lesson_code

    def set_lesson_code(self, lesson_code):
        self._lesson_code = lesson_code

    def get_teacher_of_lesson(self):
        return self._teacher_of_lesson

    def set_teacher_of_lesson(self, teacher_of_lesson):
        self._teacher_of_lesson = teacher_of_lesson

    def get_class_schedule(self):
        return self._class_schedule

    def set_class_schedule(self, class_schedule):
        self._class_schedule = class_schedule

    def add_to_class_schedule(self, class_time):
        self._class_schedule.append(class_time)

    def remove_from_class_schedule(self, class_time):
        self._class_schedule.remove(class_time)

    def get_location(self):
        return self._location

    def set_location(self, faculty_name, room_name):
        self._location['faculty_name'] = faculty_name
        self._location['room_name'] = room_name

    def get_exam_info(self):
        return self._exam_info

    def set_exam_info(self, faculty_name, room_name, time):
        exam_location = {'faculty_name': faculty_name, 'room_name': room_name}
        self._exam_info['location'] = exam_location
        self._exam_info['time'] = time

    def get_number_of_total_units(self):
        return self._number_of_total_units

    def set_number_of_total_units(self, number_of_total_units):
        self._number_of_total_units = number_of_total_units

    def get_number_of_theoretical_units(self):
        return self._number_of_theoretical_units

    def set_number_of_theoretical_units(self, number_of_theoretical_units):
        self._number_of_theoretical_units = number_of_theoretical_units

    def get_number_of_practical_units(self):
        return self._number_of_practical_units

    def set_number_of_practical_units(self, number_of_practical_units):
        self._number_of_theoretical_units = number_of_practical_units

    def get_education_group(self):
        return self._education_group

    def set_education_group(self, education_group):
        self._education_group = education_group

    def get_field_name(self):
        return self._field_name

    def set_field_name(self, field_name):
        self._field_name = field_name

    def get_allowed_fields(self):
        return self._allowed_fields

    def set_allowed_fields(self, allowed_fields):
        self._allowed_fields = allowed_fields

    def add_to_allowed_fields(self, new_field):
        self._allowed_fields.append(new_field)

    def remove_from_allowed_fields(self, field):
        self._allowed_fields.remove(field)

    def get_tuition(self):
        return self._tuition

    def set_tuition(self, tuition):
        self._tuition = tuition

    def __str__(self):
        def iterate_list(li):
            message = ""
            for index, item in enumerate(li):
                message += f"{item}" if index == len(li)-1 else f"{item}, "
            return message

        return f"Lesson: {self._lesson_name} ({self._lesson_type})\n" \
               f"\tLesson code: {self._lesson_code} | Type: {self._lesson_type_in_its_field}\n" \
               f"\tUnits number: {self._number_of_total_units} | Theoretical: {self._number_of_theoretical_units} / " \
               f"Practical: {self._number_of_practical_units}\n" \
               f"\tEducation group: {self._education_group}, Field: {self._field_name}\n" \
               f"\tTeacher: {self._teacher_of_lesson}\n" \
               f"\tClass schedule: {iterate_list(self._class_schedule)}\n" \
               f"\tClass location: {self._location.get('faculty_name')}, {self._location.get('room_name')}\n" \
               f"\tExam: Time: {self._exam_info.get('time')}\n" \
               f"\t      Location: {self._exam_info.get('location').get('faulty_name')}, " \
               f"{self._exam_info.get('location').get('room_name')}\n" \
               f"\tAllowed fields to choice: \n" \
               f"\t{iterate_list(self._allowed_fields)}\n" \
               f"\tTuition: {self._tuition} Rial\n"
