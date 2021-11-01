class Dictionaries:

    def __init__(self):
        self._genders_dict = {
            'male': 'Male',
            'female': 'Female',
            'other': 'Other'
        }

        self._degree_levels_dict = {
            'technical_college': 'Technical College',
            'vocational_college': 'Vocational College',
            'art_college': 'Art College',
            'teacher_training_college': 'Teacher Training College',
            'diploma': 'Diploma',
            'associate_in_art': 'AA (associate)',
            'associate_in_science': 'AS (associate)',
            'bachelor_in_art': 'BA (bachelor)',
            'bachelor_in_science': 'BS (bachelor)',
            'master_in_art': 'MA (master)',
            'master_in_science': 'MS (master)',
            'doctoral': 'Doctoral',
            'postdoc': 'Postdoc'
        }

        self._marital_status_dict = {
            'single': 'Single',
            'married': 'Married',
            'widowed': 'Widowed',
            'divorced': 'Divorced'
        }

        self._nationalities_dict = {
            'afghan': 'Afghan',
            'chinese': 'Chinese',
            'egyptian': 'Egyptian',
            'iraqi': 'Iraqi',
            'indian': 'Indian'
        }

        self._religions_dict = {
            'christianity': 'Christianity',
            'islam': 'Islam',
            'unaffiliated': 'Unaffiliated',
            'hinduism': 'Hinduism',
            'other': 'Other religions'
        }

        self._physical_conditions_dict = {
            'healthy': 'Healthy',
            'physical_weakness': 'Physical Weakness',
            'disability': 'Disability'
        }

        self._faculty_names_dict = {
            'architecture_and_urban_planning': 'Architecture and Urban Planning',
            'civil_and_water_and_environmental_engineering': 'Civil, Water and Environmental Engineering',
            'computer_science_and_engineering': 'Computer Science and Engineering',
            'electrical_engineering': 'Electrical Engineering',
            'mechanical_and_energy_engineering': 'Mechanical and Energy Engineering',
            'new_technologies_and_aerospace_engineering​': 'New Technologies and Aerospace Engineering​',
            'nuclear_engineering': 'Nuclear Engineering',
            'law': 'Law',
            'letters_and_human_sciences': 'Letters and Human Sciences',
            'theology_and_religious_studies': 'Theology and Religious Studies',
            'life_sciences_and_biotechnology': 'Life Sciences and Biotechnology',
            'chemistry_and_petroleum_sciences': 'Chemistry and Petroleum Sciences',
            'mathematical_sciences': 'Mathematical Sciences',
            'earth_sciences': 'Earth Sciences',
            'physics': 'Physics',
            'economics_and_political_sciences': 'Economics and Political Sciences',
            'education_and_psychology': 'Education and Psychology',
            'management_and_accounting': 'Management and Accounting',
            'sport_sciences_and_health': 'Sport Sciences and Health'
        }

        self._faculty_codes_dict = {
            'architecture_and_urban_planning': 10,
            'civil_and_water_and_environmental_engineering': 11,
            'computer_science_and_engineering': 12,
            'electrical_engineering': 13,
            'mechanical_and_energy_engineering': 14,
            'new_technologies_and_aerospace_engineering​': 15,
            'nuclear_engineering': 16,
            'law': 17,
            'letters_and_human_sciences': 18,
            'theology_and_religious_studies': 19,
            'life_sciences_and_biotechnology': 20,
            'chemistry_and_petroleum_sciences': 21,
            'mathematical_sciences': 22,
            'earth_sciences': 23,
            'physics': 24,
            'economics_and_political_sciences': 25,
            'education_and_psychology': 26,
            'management_and_accounting': 27,
            'sport_sciences_and_health': 28
        }

        self._sections_dict = {
            'associate_in_art': 'AA (associate)',
            'associate_in_science': 'AS (associate)',
            'bachelor_in_art': 'BA (bachelor)',
            'bachelor_in_science': 'BS (bachelor)',
            'master_in_art': 'MA (master)',
            'master_in_science': 'MS (master)',
            'doctoral': 'Doctoral',
            'postdoc': 'Postdoc'
        }

        self._courses_dict = {
            'bursary_student': 'Bursary Student',
            'tuition_student': 'Tuition Student'
        }

        self._units_number_for_graduation_base_field_associate = {
            'architecture_and_urban_planning': 10,
            'civil_and_water_and_environmental_engineering': 11,
            'computer_science_and_engineering': 12,
            'electrical_engineering': 13,
            'mechanical_and_energy_engineering': 14,
            'new_technologies_and_aerospace_engineering​': 15,
            'nuclear_engineering': 16,
            'law': 17,
            'letters_and_human_sciences': 18,
            'theology_and_religious_studies': 19,
            'life_sciences_and_biotechnology': 20,
            'chemistry_and_petroleum_sciences': 21,
            'mathematical_sciences': 22,
            'earth_sciences': 23,
            'physics': 24,
            'economics_and_political_sciences': 25,
            'education_and_psychology': 26,
            'management_and_accounting': 27,
            'sport_sciences_and_health': 28
        }

        self._faculty_codes_dict = {
            'architecture_and_urban_planning': 10,
            'civil_and_water_and_environmental_engineering': 11,
            'computer_science_and_engineering': 12,
            'electrical_engineering': 13,
            'mechanical_and_energy_engineering': 14,
            'new_technologies_and_aerospace_engineering​': 15,
            'nuclear_engineering': 16,
            'law': 17,
            'letters_and_human_sciences': 18,
            'theology_and_religious_studies': 19,
            'life_sciences_and_biotechnology': 20,
            'chemistry_and_petroleum_sciences': 21,
            'mathematical_sciences': 22,
            'earth_sciences': 23,
            'physics': 24,
            'economics_and_political_sciences': 25,
            'education_and_psychology': 26,
            'management_and_accounting': 27,
            'sport_sciences_and_health': 28
        }

    def get_genders_dict(self):
        return self._genders_dict

    def get_degree_levels_dict(self):
        return self._degree_levels_dict

    def get_marital_status_dict(self):
        return self._marital_status_dict

    def get_nationalities_dict(self):
        return self._nationalities_dict

    def get_religions_dict(self):
        return self._religions_dict

    def get_physical_conditions_dict(self):
        return self._physical_conditions_dict

    def get_faculty_names_dict(self):
        return self._faculty_names_dict

    def set_faculty_names_dict(self, faculty_names_dict):
        self._faculty_names_dict = faculty_names_dict

    def add_to_faculty_names_dict(self, new_faculty_name_dict):
        self._faculty_names_dict.update(new_faculty_name_dict)

    def remove_from_faculty_names_dict(self, faculty_name_dict):
        self._faculty_names_dict.pop(list(faculty_name_dict.keys())[0], None)

    def get_faculty_codes_dict(self):
        return self._faculty_codes_dict

    def set_faculty_codes_dict(self, faculty_codes_dict):
        self._faculty_codes_dict = faculty_codes_dict

    def add_to_faculty_codes_dict(self, new_faculty_code_dict):
        self._faculty_codes_dict.update(new_faculty_code_dict)

    def remove_from_faculty_codes_dict(self, faculty_code_dict):
        self._faculty_codes_dict.pop(list(faculty_code_dict.keys())[0], None)

    def get_sections_dict(self):
        return self._sections_dict

    def set_sections_dict(self, sections_dict):
        self._sections_dict = sections_dict

    def add_to_sections_dict(self, new_sections_dict):
        self._sections_dict.update(new_sections_dict)

    def remove_from_sections_dict(self, sections_dict):
        self._sections_dict.pop(list(sections_dict.keys())[0], None)

    def get_courses_dict(self):
        return self._courses_dict

    def set_courses_dict(self, courses_dict):
        self._courses_dict = courses_dict

    def add_to_courses_dict(self, new_courses_dict):
        self._courses_dict.update(new_courses_dict)

    def remove_from_courses_dict(self, courses_dict):
        self._courses_dict.pop(list(courses_dict.keys())[0], None)
