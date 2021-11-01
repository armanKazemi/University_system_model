from models.University.Building import Building


class Faculty(Building):
    """
    Model of FACULTY, information of faculty.
    """

    def __init__(self):
        super().__init__()
        self._faculty_code = ''  # faculty code
        self._fields_list = []   # faculty fields list (type of indexes: Field)
        self._faculty_average = 0.0  # faculty average

    def get_faculty_code(self):
        return self._faculty_code

    def set_faculty_code(self, faculty_code):
        self._faculty_code = faculty_code

    def get_fields_list(self):
        return self._fields_list

    def set_fields_list(self, fields_list):
        self._fields_list = fields_list

    def add_to_fields_list(self, new_field):
        self._fields_list.append(new_field)

    def remove_from_fields_list(self, field):
        self._fields_list.remove(field)

    def get_faculty_average(self):
        return self._faculty_average

    def set_faculty_average(self, faculty_average):
        self._faculty_average = faculty_average

    def __str__(self):
        def iterate_list(list_name, li):
            message = ""
            for index, item in enumerate(li):
                message += f"\t{list_name} {index + 1}\n" \
                           f" {item}\n"
            return message

        return super().__str__() + f"\tFaculty code: {self._faculty_code}\n" \
                                   f"\tFaculty average: {self._faculty_average}\n" \
                                   f"\tFields list:\n" \
                                   f"{iterate_list('Field', self._fields_list)}\n"
