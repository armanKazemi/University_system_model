import datetime


class University:
    """
    Model of UNIVERSITY, information of university.
    """

    def __init__(self):
        super().__init__()
        self._university_name = ''  # university name
        self._university_address = ''  # university address
        self._date_of_establishment = None  # university establishment's date
        self._buildings_list = []   # university buildings list (type of indexes: Building)
        self._faculties_list = []   # university faculties list (type of indexes: Faculty)
        self._public_relation_ways_list = []  # public relation ways list (type of indexes: String)
        self._web_address = ''      # university web address
        self._descriptions = ''     # university descriptions

    def get_university_name(self):
        return self._university_name

    def set_university_name(self, university_name):
        self._university_name = university_name

    def get_university_address(self):
        return self._university_address

    def set_university_address(self, university_address):
        self._university_address = university_address

    def get_date_of_establishment(self):
        return self._date_of_establishment

    def set_date_of_establishment(self, year, month, day):
        self._date_of_establishment = datetime.datetime(year, month, day)

    def get_buildings_list(self):
        return self._buildings_list

    def set_buildings_list(self, buildings_list):
        self._buildings_list = buildings_list

    def add_to_buildings_list(self, new_building):
        self._buildings_list.append(new_building)

    def remove_from_buildings_list(self, building):
        self._buildings_list.remove(building)

    def get_faculties_list(self):
        return self._faculties_list

    def set_faculties_list(self, faculties_list):
        self._faculties_list = faculties_list

    def add_to_faculties_list(self, new_faculty):
        self._faculties_list.append(new_faculty)

    def remove_from_faculties_list(self, faculty):
        self._faculties_list.remove(faculty)

    def get_public_relation_ways_list(self):
        return self._public_relation_ways_list

    def set_public_relation_ways_list(self, public_relation_ways_list):
        self._public_relation_ways_list = public_relation_ways_list

    def add_to_public_relation_ways_list(self, new_way):
        self._public_relation_ways_list.append(new_way)

    def remove_from_public_relation_ways_list(self, way):
        self._public_relation_ways_list.remove(way)

    def get_web_address(self):
        return self._web_address

    def set_web_address(self, web_address):
        self._web_address = web_address

    def get_descriptions(self):
        return self._descriptions

    def set_descriptions(self, descriptions):
        self._descriptions = descriptions

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

        return f"{self._university_name} university\n" \
               f"Address: {self._university_address}\n" \
               f"Date of establishment: {self._date_of_establishment}\n" \
               f"Web address: {self._web_address}\n" \
               f"Buildings list:\n" \
               f"{iterate_list('Building', self._buildings_list)}\n" \
               f"Faculties list:\n" \
               f"{iterate_list('Faculty', self._faculties_list)}\n" \
               f"Public relation ways:\n" \
               f"{iterate_list('', self._public_relation_ways_list)}\n" \
               f"Descriptions:\n" \
               f"\t{self._descriptions}\n"
