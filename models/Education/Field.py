class Field:
    """
    Model of FIELD, field's information.
    """

    def __init__(self):
        self._field_name = ''            # filed name
        self._field_code = ''            # field code
        self._faculty_name = ''          # field faculty name
        self._education_group_name = ''  # field education group name
        self._lessons_list = []          # field lessons list (type of indexes: Lesson)
        self._employees_list = []        # field employees list (type of indexes: Employee)
        self._teachers_list = []         # field teachers list (type of indexes: Teacher)
        self._supervisors_list = []      # field supervisors list (type of indexes: Teacher)
        self._science_committees_list = []  # field science committees list (type of indexes: Teacher)
        self._grade_level = ''           # filed grade level [AA/AS/BA/BS/MA/MS/Doctoral/Postdoc]
        self._students_list = []         # filed students list (type of indexes: Student)
        self._field_average = 0.0        # field average
        self._number_of_units_for_graduation_interval = {}   # (key:begin/end of period, value:number of units)
        self._education_administrator_phone_numbers_list = []  # (type of indexes: String)
        self._education_administrator_fax_numbers_list = []  # (type of indexes: String)
        self._education_administrator_email = ''             # field email

    def get_field_name(self):
        return self._field_name

    def set_field_name(self, field_name):
        self._field_name = field_name

    def get_field_code(self):
        return self._field_code

    def set_field_code(self, field_code):
        self._field_code = field_code

    def get_faculty_name(self):
        return self._faculty_name

    def set_faculty_name(self, faculty_name):
        self._faculty_name = faculty_name

    def get_education_group_name(self):
        return self._education_group_name

    def set_education_group_name(self, education_group_name):
        self._education_group_name = education_group_name

    def get_lessons_list(self):
        return self._lessons_list

    def set_lessons_list(self, lessons_list):
        self._lessons_list = lessons_list

    def add_to_lessons_list(self, new_lesson):
        self._lessons_list.append(new_lesson)

    def remove_from_lessons_list(self, lesson):
        self._lessons_list.remove(lesson)

    def get_employees_list(self):
        return self._employees_list

    def set_employees_list(self, employees_list):
        self._employees_list = employees_list

    def add_to_employees_list(self, new_employee):
        self._employees_list.append(new_employee)

    def remove_from_employees_list(self, employee):
        self._employees_list.remove(employee)

    def get_teachers_list(self):
        return self._teachers_list

    def set_teachers_list(self, teachers_list):
        self._teachers_list = teachers_list

    def add_to_teachers_list(self, new_teacher):
        self._teachers_list.append(new_teacher)

    def remove_from_teachers_list(self, teacher):
        self._teachers_list.remove(teacher)

    def get_supervisors_list(self):
        return self._supervisors_list

    def set_supervisors_list(self, supervisors_list):
        self._supervisors_list = supervisors_list

    def add_to_supervisors_list(self, new_supervisor):
        self._supervisors_list.append(new_supervisor)

    def remove_from_supervisors_list(self, supervisor):
        self._supervisors_list.remove(supervisor)

    def get_science_committees_list(self):
        return self._science_committees_list

    def set_science_committees_list(self, science_committees_list):
        self._science_committees_list = science_committees_list

    def add_to_science_committees_list(self, new_science_committee):
        self._science_committees_list.append(new_science_committee)

    def remove_from_science_committees_list(self, science_committee):
        self._science_committees_list.remove(science_committee)

    def get_grade_level(self):
        return self._grade_level

    def set_grade_level(self, grade_level):
        self._grade_level = grade_level

    def get_students_list(self):
        return self._students_list

    def set_students_list(self, students_list):
        self._students_list = students_list

    def add_to_students_list(self, new_student):
        self._students_list.append(new_student)

    def remove_from_students_list(self, student):
        self._students_list.remove(student)

    def get_field_average(self):
        return self._field_average

    def set_field_average(self, field_average):
        self._field_average = field_average

    def get_number_of_units_for_graduation_interval(self):
        return self._number_of_units_for_graduation_interval

    def set_number_of_units_for_graduation_interval(self, begin, end):
        self._number_of_units_for_graduation_interval['begin'] = begin
        self._number_of_units_for_graduation_interval['end'] = end

    def get_education_administrator_phone_numbers_list(self):
        return self._education_administrator_phone_numbers_list

    def set_education_administrator_phone_numbers_list(self, phone_numbers_list):
        self._education_administrator_phone_numbers_list = phone_numbers_list

    def add_to_education_administrator_phone_numbers_list(self, new_phone_number):
        self._education_administrator_phone_numbers_list.append(new_phone_number)

    def remove_from_education_administrator_phone_numbers_list(self, phone_number):
        self._education_administrator_phone_numbers_list.remove(phone_number)

    def get_education_administrator_fax_numbers_list(self):
        return self._education_administrator_fax_numbers_list

    def set_education_administrator_fax_numbers_list(self, fax_numbers_list):
        self._education_administrator_fax_numbers_list = fax_numbers_list

    def add_to_education_administrator_fax_numbers_list(self, new_fax_number):
        self._education_administrator_fax_numbers_list.append(new_fax_number)

    def remove_from_education_administrator_fax_numbers_list(self, fax_number):
        self._education_administrator_fax_numbers_list.remove(fax_number)

    def get_education_administrator_email(self):
        return self._education_administrator_email

    def set_education_administrator_email(self, email):
        self._education_administrator_email = email

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

        return f"Field {self._field_name} in {self._grade_level} level | code: {self._field_code}\n" \
               f"Education group: {self._education_group_name} in {self._faculty_name} faculty\n" \
               f"Lessons list:\n" \
               f"{iterate_list('Lesson', self._lessons_list)}\n" \
               f"Employees list:\n" \
               f"{iterate_list('Employee', self._employees_list)}\n" \
               f"Teachers list:\n" \
               f"{iterate_list('Teacher', self._teachers_list)}\n" \
               f"Supervisors list:\n" \
               f"{iterate_list('Supervisor', self._supervisors_list)}\n" \
               f"Science committees list:\n" \
               f"{iterate_list('Science committee', self._science_committees_list)}\n" \
               f"Students list:\n" \
               f"{iterate_list('Student', self._students_list)}\n" \
               f"Number of units for graduation: " \
               f"[{self._number_of_units_for_graduation_interval.get('begin')}, " \
               f"{self._number_of_units_for_graduation_interval.get('end')}]\n" \
               f"Field average: {self._field_average}\n" \
               f"Phone numbers list:\n" \
               f"{iterate_list('', self._education_administrator_phone_numbers_list)}\n" \
               f"Fax numbers list:\n" \
               f"{iterate_list('', self._education_administrator_fax_numbers_list)}\n" \
               f"Email address: {self._education_administrator_email}\n"
