from models.Person.UniversityUser import UniversityUser


class Employee(UniversityUser):
    """
    Model of EMPLOYEE specific information.
    """

    def __init__(self):
        super().__init__()
        self._post = ''                 # employee's post name
        self._office_address = ''       # office address. (in university)
        self._office_phone_number = ''  # office phone number
        self._office_fax_number = ''    # office fax number
        self._salary_base_amount = 0.0  # salary base amount
        self._salary_per_overtime_hour_amount = 0.0  # salary per overtime hour amount
        self._overtime_hours = 0.0      # overtime hours
        self._vacation_numbers_per_year = 0  # allowed vacation numbers per year
        self._work_history = []         # work history list (type of indexes: String)

    def get_post(self):
        return self._post

    def set_post(self, post):
        self._post = post

    def get_office_address(self):
        return self._office_address

    def set_office_address(self, office_address):
        self._office_address = office_address

    def get_office_phone_number(self):
        return self._office_phone_number

    def set_office_phone_number(self, office_phone_number):
        self._office_phone_number = office_phone_number

    def get_office_fax_number(self):
        return self._office_fax_number

    def set_office_fax_number(self, office_fax_number):
        self._office_fax_number = office_fax_number

    def get_salary_base_amount(self):
        return self._salary_base_amount

    def set_salary_base_amount(self, salary_base_amount):
        self._salary_base_amount = salary_base_amount

    def get_salary_per_overtime_hour_amount(self):
        return self._salary_per_overtime_hour_amount

    def set_salary_per_overtime_hour_amount(self, salary_per_overtime_amount):
        self._salary_per_overtime_hour_amount = salary_per_overtime_amount

    def get_overtime_hours(self):
        return self._overtime_hours

    def set_overtime_hours(self, overtime_hours):
        self._overtime_hours = overtime_hours

    def get_vacation_numbers_per_year(self):
        return self._vacation_numbers_per_year

    def set_vacation_numbers_per_year(self, vacation_numbers_per_year):
        self._vacation_numbers_per_year = vacation_numbers_per_year

    def get_work_history(self):
        return self._work_history

    def set_work_history(self, work_history):
        self._work_history = work_history

    def add_to_work_history(self, new_work_history):
        self._work_history.append(new_work_history)

    def remove_from_work_history(self, work_history):
        self._work_history.remove(work_history)

    def __str__(self):
        def iterate_list(li):
            message = ""
            for index, item in enumerate(li):
                message += f"\t{index + 1}. {item}\n"
            return message

        return super().__str__() + \
               f"\n" \
               f"Employee's Information:\n" \
               f"\tPost: {self._post}\n" \
               f"\tOffice address: {self._office_address}\n" \
               f"\tOffice phone number: {self._office_phone_number}\n" \
               f"\tOffice fax number: {self._office_fax_number}\n" \
               f"\tSalary base amount: {self._salary_base_amount}\n" \
               f"\tSalary amount for per overtime hour: {self._salary_per_overtime_hour_amount}\n" \
               f"\tOvertime hours: {self._overtime_hours}\n" \
               f"\tVacation number: {self._vacation_numbers_per_year}\n" \
               f"\tWork history: \n" \
               f"{iterate_list(self._work_history)}\n"
