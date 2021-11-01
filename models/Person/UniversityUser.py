from datetime import datetime


class UniversityUser:
    """
    Model of base information of university user. Employees, Teachers and Students.
    """

    def __init__(self):
        self._first_name = ''             # first name
        self._nick_name = ''              # nick name
        self._last_name = ''              # last name
        self._father_name = ''            # father's name
        self._birthday = None             # birthday date (type: datetime)
        self._gender = ''                 # gender
        self._grade_level = ''            # grade level of education
        self._marital_status = ''         # marital status
        self._nationality = ''            # his/her nationality
        self._identification_number = ''  # identification code. (iranian: ID number, others: passport number)
        self._religion = ''               # religion
        self._physical_condition = ''     # he/she is healthy or have a disability
        self._phone_number = ''           # main phone number
        self._second_phone_number = ''    # alternative phone number
        self._web_user_id = ''            # specific username for entering to university website
        self._web_password = ''           # specific password for entering to university website
        self._user_earmark = ''           # specific earmark for each student
        self._university_email = ''       # specific university email for each student
        self._bank_account_number = ''    # bank account number, for deposit or withdraw
        self._university_name = ''        # university name
        self._building_name = ''          # building name
        self._faculty_code = 0            # faculty code
        self._education_group = ''        # education group name
        self._register_date = None        # date of register in university
        self._email_address = ''          # personal email address
        self._home_address = ''           # home address
        self._personal_photo = None       # personal photo [3*4]. (type: File)
        self._id_photo = None             # iranian: SHENASNAME, others: Visa photo. (type: File)
        self._identity_card_photo = None  # id card / passport. (type: File)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name.capitalize().strip()

    def get_nick_name(self):
        return self._nick_name

    def set_nick_name(self, nick_name):
        self._nick_name = nick_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name.capitalize().strip()

    def get_father_name(self):
        return self._father_name

    def set_father_name(self, father_name):
        self._father_name = father_name.capitalize().strip()

    def get_birthday(self):
        return self._birthday

    def set_birthday(self, year, month, day):
        self._birthday = datetime(year, month, day)

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender.capitalize().strip()

    def get_grade_level(self):
        return self._grade_level

    def set_grade_level(self, grade_level):
        self._grade_level = grade_level

    def get_marital_status(self):
        return self._marital_status

    def set_marital_status(self, marital_status):
        self._marital_status = marital_status.capitalize().strip()

    def get_nationality(self):
        return self._nationality

    def set_nationality(self, nationality):
        self._nationality = nationality.capitalize().strip()

    def get_identification_number(self):
        return self._identification_number

    def set_identification_number(self, identification_number):
        self._identification_number = identification_number

    def get_religion(self):
        return self._religion

    def set_religion(self, religion):
        self._religion = religion.capitalize().strip()

    def get_physical_condition(self):
        return self._physical_condition

    def set_physical_condition(self, physical_condition):
        self._physical_condition = physical_condition.capitalize().strip()

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def get_second_phone_number(self):
        return self._second_phone_number

    def set_second_phone_number(self, second_phone_number):
        self._second_phone_number = second_phone_number

    def get_web_user_id(self):
        return self._web_user_id

    def set_web_user_id(self, web_user_id):
        self._web_user_id = web_user_id

    def get_web_password(self):
        return self._web_password

    def set_web_password(self, web_password):
        self._web_password = web_password

    def get_user_earmark(self):
        return self._user_earmark

    def set_user_earmark(self, user_earmark):
        self._user_earmark = user_earmark

    def get_university_email(self):
        return self._university_email

    def set_university_email(self, university_email):
        self._university_email = university_email

    def get_bank_account_number(self):
        return self._bank_account_number

    def set_bank_account_number(self, bank_account_number):
        self._bank_account_number = bank_account_number

    def get_university(self):
        return self._university_name

    def set_university(self, university_name):
        self._university_name = university_name.capitalize().strip()

    def get_building_name(self):
        return self._building_name

    def set_building_name(self, building_name):
        self._building_name = building_name.capitalize().strip()

    def get_faculty_code(self):
        return self._faculty_code

    def set_faculty_code(self, faculty_code):
        self._faculty_code = faculty_code

    def get_education_group(self):
        return self._education_group

    def set_education_group(self, education_group):
        self._education_group = education_group.capitalize().strip()

    def get_register_date(self):
        return self._register_date

    def set_register_date(self, year, month, day):
        self._register_date = datetime(year, month, day)

    def get_email_address(self):
        return self._email_address

    def set_email_address(self, email_address):
        self._email_address = email_address

    def get_home_address(self):
        return self._home_address

    def set_home_address(self, home_address):
        self._home_address = home_address

    def get_personal_photo(self):
        return self._personal_photo

    def set_personal_photo(self, personal_photo):
        self._personal_photo = personal_photo

    def get_id_photo(self):
        return self._id_photo

    def set_id_photo(self, id_photo):
        self._id_photo = id_photo

    def get_identity_card_photo(self):
        return self._identity_card_photo

    def set_identity_card_photo(self, identity_card_photo):
        self._identity_card_photo = identity_card_photo

    def __str__(self):
        return f"New {self._university_name} University user: {self._first_name} {self._last_name}, " \
               f"Nick name: {self._nick_name}\n" \
               f"\n" \
               f"Personal Information: \n" \
               f"\tFather's name: {self._father_name}\n" \
               f"\tBirthday: {self._birthday}\n" \
               f"\tGender: {self._gender}\n" \
               f"\tNationality: {self._nationality}\n" \
               f"\tReligion: {self._religion}" \
               f"\tMarital status: {self._marital_status}\n" \
               f"\tPhysical condition: {self._physical_condition}\n" \
               f"\tGrade level: {self._grade_level}\n" \
               f"\tIdentification number: {self._identification_number}\n" \
               f"\tPhone number: {self._phone_number}\n" \
               f"\tSecond phone number: {self._second_phone_number}\n" \
               f"\tBank account number: {self._bank_account_number}\n" \
               f"\tEmail address: {self._email_address}\n" \
               f"\tHome address: {self._home_address}\n" \
               f"\n" \
               f"University Information:\n" \
               f"\tWeb username: {self._web_user_id}\n" \
               f"\tWeb password: {self._web_password}\n" \
               f"\tUser earmark: {self._user_earmark}\n" \
               f"\tUniversity email: {self._university_email}\n" \
               f"\tBuilding name: {self._building_name}\n" \
               f"\tFaculty code(not for all employees): {self._faculty_code}\n" \
               f"\tEducation group(not for all employees): {self._education_group}\n" \
               f"\tRegister date in university: {self._register_date}\n"

