"""system module."""
import sys
import csv
from operator import attrgetter
import os
from deserialiser_csv import main_serializer


class Control:
    """Controller Part : data handling from view and Models."""

    def __init__(self):
        """variables."""

        self.home_object = None
        self.path = os.path.abspath("in_file.csv")
        self.data_sorted = []
        self.list_data = []
        self.data_cleaned = []
        self.final_list = []

        # Open the file previously created
        with open('DATAS/in_file.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                self.list_data.append(row)

    def input_choice_first_menu_from_view(self):
        """
               Function to verify response from user ( View ).

               We confirm 3 choices: 1 - display all homes
                                     2 - can search
                                     Q - can Quit

               """
        from view import main_interface

        choix_option = main_interface()
        if choix_option == '1':
            self.home_view_all()
            return self.input_choice_first_menu_from_view()
        elif choix_option == '2':
            self.search_option_filter_with_value_from_view()
        elif choix_option == 'Q':
            sys.exit()
        else:
            print("Attention la valeur n'est pas bonne")
            return self.input_choice_first_menu_from_view()

    def clean_data_and_make_object(self):
        """
        This function have purpose to handle data, sort data, and create a new format with it.
        :return: list of data sorted and cleaned for custumers
        """
        from model import Home

        for obj in self.list_data:
            # Use instance our class for each iteration
            self.home_object = Home(property=obj[0], building_id=obj[1],
                                    owner_acquisition_date=obj[2],
                                    street1=obj[3], city=obj[4],
                                    zip=obj[5],
                                    lastname=obj[6], firstname=obj[7].lower(),
                                    email=obj[8])
            self.data_cleaned.append(self.home_object)

        # we sorted all data by two instance way
        self.data_sorted = list(sorted(set(self.data_cleaned),
                                       key=attrgetter('building_id', 'lastname'),
                                       reverse=True))

        for i in self.data_sorted:
            # Here we created a last list for delete all duplicat in our previously list and check it.

            if i.building_id and i.property not in self.final_list:
                self.final_list.append(i)

        return self.final_list

    def loop_for_table_in_terminal(self, target):
        """
        This function has purpose to create good table with function from view part
        :param target: Data's source

        """
        from view import prt_width

        for i in target:
            prt_width(i.property, 7)
            prt_width(i.building_id, 11)
            prt_width(i.owner_acquisition_date, 22)
            prt_width(i.street1, 31)
            prt_width(i.city, 22)
            prt_width(i.zip, 25)
            prt_width(i.lastname, 25)
            prt_width(i.firstname, 25)
            prt_width(i.email, 25)
            prt_width('\n', 1)

    def home_view_all(self):
        """
        Function for display all home
        :return: table for terminal
        """
        return self.loop_for_table_in_terminal(self.clean_data_and_make_object())

    def cleaned_function_for_search_and_optimized(self, header, column):
        self.loop_for_table_in_terminal(header)
        self.loop_for_table_in_terminal(column)

    def search_option_filter_with_value_from_view(self):
        """
        This function has purpose tu handling and create statement to verify the user's input
        :return:  print the menu for user always after
        """
        from view import search_for_user_param

        header = list(filter(lambda home: home.property == 'property', self.final_list
                             ))
        search_for_filter, value_for_filter = search_for_user_param()
        value_for_filter_striped = value_for_filter.strip()
        search_for_filter_striped = search_for_filter.strip()

        if search_for_filter_striped == 'property':
            property = list(filter(lambda home: home.property == value_for_filter_striped, self.final_list
                                   ))
            self.cleaned_function_for_search_and_optimized(header, property)

        elif search_for_filter_striped == 'building_id':
            building = list(filter(lambda home: home.building_id == value_for_filter_striped, self.final_list
                                   ))
            self.cleaned_function_for_search_and_optimized(header, building)

        elif search_for_filter_striped == 'owner_acquisition_date':
            owner_acquisition = list(
                filter(lambda home: home.owner_acquisition_date == value_for_filter_striped, self.final_list
                       ))
            self.cleaned_function_for_search_and_optimized(header, owner_acquisition)

        elif search_for_filter_striped == 'street1':
            street = list(filter(lambda home: home.street1 == value_for_filter_striped, self.final_list
                                 ))
            self.cleaned_function_for_search_and_optimized(header, street)

        elif search_for_filter_striped == 'city':
            city = list(filter(lambda home: home.city == value_for_filter_striped, self.final_list
                               ))
            self.cleaned_function_for_search_and_optimized(header, city)

        elif search_for_filter_striped == 'zip':
            zip = list(filter(lambda home: home.zip == value_for_filter_striped, self.final_list
                              ))
            self.cleaned_function_for_search_and_optimized(header, zip)

        elif search_for_filter_striped == 'lastname':
            lastname = list(filter(lambda home: home.lastname == value_for_filter_striped, self.final_list
                                   ))
            self.cleaned_function_for_search_and_optimized(header, lastname)

        elif search_for_filter_striped == 'firstname':
            firstname = list(filter(lambda home: home.firstname == value_for_filter_striped, self.final_list
                                    ))
            self.cleaned_function_for_search_and_optimized(header, firstname)

        elif search_for_filter_striped == 'email':
            email = list(filter(lambda home: home.email == value_for_filter_striped, self.final_list
                                ))
            self.cleaned_function_for_search_and_optimized(header, email)

        else:
            print("The word's section match with anything !!! retry please")

        return self.input_choice_first_menu_from_view()


def main_c():
    """
    Master function

    """
    c = Control()
    c.input_choice_first_menu_from_view()


if __name__ == "__main__":
    # Import function from deserializer for clean file to handling and run the app.

    main_serializer()
    main_c()
