class Room:
    """
    Model of ROOM, information of types of room in university.
    """

    def __init__(self):
        self._building_name = ''  # building name
        self._room_address = ''   # room address
        self._room_name = ''      # room name
        self._room_type = ''      # room type[Classroom/Laboratory/Computer room/Gym/Library/Study room/Amphitheater]
        self._room_plans = {}     # room time table (key:session name, value:Time)
        self._capacity = 0        # room capacity (based on person's number)
        self._has_projector = False  # has room projector
        self._facilities = []     # room facilities (type of indexes: String)
        self._descriptions = ''   # room descriptions

    def get_building_name(self):
        return self._building_name

    def set_building_name(self, building_name):
        self._building_name = building_name

    def get_room_address(self):
        return self._room_address

    def set_room_address(self, room_address):
        self._room_address = room_address

    def get_room_name(self):
        return self._room_name

    def set_room_name(self, room_name):
        self._room_name = room_name

    def get_room_type(self):
        return self._room_type

    def set_room_type(self, room_type):
        self._room_type = room_type

    def get_room_plans(self):
        return self._room_plans

    def set_room_plans(self, room_plans):
        self._room_plans = room_plans

    def add_to_room_plans(self, new_key, new_plan):
        self._room_plans[new_key] = new_plan

    def removed_from_room_plans(self, plan_key):
        self._room_plans.pop(plan_key, None)

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, capacity):
        self._capacity = capacity

    def has_projector(self):
        return self._has_projector

    def set_projector_status(self, has_projector):
        self._has_projector = has_projector

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
        def iterate_list(li):
            message = ""
            for index, item in enumerate(li):
                message += f"\t{index+1}. {item}\n"
            return message

        def iterate_dict(di):
            message = ""
            for key in di:
                message += f"\t{key}: {di.get(key)}\n"
            return message

        return f"Room {self._room_name}, Type: {self._room_type}\n in {self._building_name}, {self._room_address}\n" \
               f"\tCapacity: {self._capacity}, Has projector: {'Yes' if self._has_projector else 'No'}\n" \
               f"\tRoom plans:\n" \
               f"{iterate_dict(self._room_plans)}\n" \
               f"\tFacilities:\n" \
               f"{iterate_list(self._facilities)}\n" \
               f"\tDescriptions:\n" \
               f"\t{self._descriptions}\n"
