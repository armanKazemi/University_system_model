class Building:
    """
    Model of BUILDING, information of building.
    """

    def __init__(self):
        self._building_name = ''    # building name
        self._number_of_floors = 1  # building number of floors
        self._has_elevator = False  # elevator status
        self._has_amphitheater = False  # amphitheater status
        self._offices_list = []     # building offices list(type of indexes: Office)
        self._rooms_list = []       # building rooms list (type of indexes: Room)
        self._public_relation_ways_list = []  # public relation ways list (type of indexes: String)
        self._facilities = []       # building facilities list (type of indexes: String)
        self._descriptions = ''     # building descriptions

    def get_building_name(self):
        return self._building_name

    def set_building_name(self, building_name):
        self._building_name = building_name

    def get_number_of_floors(self):
        return self._number_of_floors

    def set_number_of_floors(self, number_of_floors):
        self._number_of_floors = number_of_floors

    def has_elevator(self):
        return self._has_elevator

    def set_elevator_status(self, has_elevator):
        self._has_elevator = has_elevator

    def has_amphitheater(self):
        return self._has_elevator

    def set_amphitheater(self, has_amphitheater):
        self._has_amphitheater = has_amphitheater

    def get_offices_list(self):
        return self._offices_list

    def set_offices_list(self, offices_list):
        self._offices_list = offices_list

    def add_to_offices_list(self, new_office):
        self._offices_list.append(new_office)

    def remove_from_offices_list(self, office):
        self._offices_list.remove(office)

    def get_rooms_list(self):
        return self._rooms_list

    def set_rooms_list(self, rooms_list):
        self._rooms_list = rooms_list

    def add_to_rooms_list(self, new_room):
        self._rooms_list.append(new_room)

    def remove_from_rooms_list(self, room):
        self._rooms_list.remove(room)

    def get_public_relation_ways_list(self):
        return self._public_relation_ways_list

    def set_public_relation_ways_list(self, public_relation_ways_list):
        self._public_relation_ways_list = public_relation_ways_list

    def add_to_public_relation_ways_list(self, new_way):
        self._public_relation_ways_list.append(new_way)

    def remove_from_public_relation_ways_list(self, way):
        self._public_relation_ways_list.remove(way)

    def get_facilities(self):
        return self._facilities

    def set_facilities(self, facilities):
        self._facilities = facilities

    def add_to_facilities(self, new_facility):
        self._facilities.append(new_facility)

    def remove_from_facilities(self, facility):
        self._facilities.remove(facility)

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

        return f"{self._building_name} building [{self._number_of_floors} floors]\n" \
               f"\tOffices list:\n" \
               f"{iterate_list('Office', self._offices_list)}\n" \
               f"\tRooms list:\n" \
               f"{iterate_list('Room', self._rooms_list)}\n" \
               f"\tHas amphitheater? {'Yes' if self._has_amphitheater else 'No'}\n" \
               f"\tHas elevator? {'Yes' if self._has_elevator else 'No'}\n" \
               f"\tPublic relation ways:\n" \
               f"{iterate_list('', self._public_relation_ways_list)}\n" \
               f"\tFacilities:\n" \
               f"{iterate_list('', self._facilities)}\n" \
               f"\tDescriptions:\n" \
               f"\t\t{self._descriptions}\n"
