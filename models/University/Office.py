from models.University.Room import Room


class Office(Room):
    """
    Model of OFFICE, for employees and teachers.
    """

    def __init__(self):
        super().__init__()
        self._office_name = ''   # office name
        self._office_type = ''   # office type [Sentry/Administrative/Office/Students room/Forum]
        self._members_list = []  # office members list (type of indexes: Employee/Teacher)

    def get_office_name(self):
        return self._office_name

    def set_office_name(self, office_name):
        self._office_name = office_name

    def get_office_type(self):
        return self._office_type

    def set_office_type(self, office_type):
        self._office_type = office_type

    def get_members_list(self):
        return self._members_list

    def set_members_list(self, members_list):
        self._members_list = members_list

    def add_to_members_list(self, new_member):
        self._members_list.append(new_member)

    def remove_from_members_list(self, member):
        self._members_list.remove(member)

    def __str__(self):
        def iterate_list(list_name, li):
            message = ""
            for index, item in enumerate(li):
                message += f"\t{list_name} {index + 1}\n" \
                           f" {item}\n"
            return message

        return super().__str__() + f"\tOffice name: {self._office_name} | Type: {self._office_type}\n" \
                                   f"\tMembers list:\n" \
                                   f"{iterate_list('Member', self._members_list)}\n"
