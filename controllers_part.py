"""system module."""
import sys
import csv
from operator import attrgetter
import os
from deserialiser_csv import main_serializer


class Control:
    """Controller Part : data traitement from view and Models."""

    def __init__(self):
        """variables."""

        self.home_object = None
        self.path = os.path.abspath("in_file.csv")
        self.data_sorted = []
        self.list_data = []
        self.data_cleaned = []
        with open('DATAS/in_file.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                self.list_data.append(row)

    def input_choice_first_menu_from_view(self):
        """
               Function to verify response from user ( View ).

               We confirm 3 choices: 1 - display all homes
                                     2 - can search

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
        from model import Home

        for obj in self.list_data:
            self.home_object = Home(property=obj[0], building_id=obj[1],
                                    owner_acquisition_date=obj[2],
                                    street1=obj[3], city=obj[4],
                                    zip=obj[5],
                                    lastname=obj[6], firstname=obj[7].lower(),
                                    email=obj[8])
            self.data_cleaned.append(self.home_object)

        self.data_sorted = list(sorted(set(self.data_cleaned),
                                       key=attrgetter('building_id', 'lastname'),
                                       reverse=True))
        return self.data_sorted

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
        '''
        Fucntion for display all home
        :return: table for terminal
        '''
        return self.loop_for_table_in_terminal(self.clean_data_and_make_object())

    def search_option_filter_with_value_from_view(self):
        """
        This function has purpose tu handling and create statement to verify the user's input
        :return:  print the menu for user always after
        """
        from view import search_for_user_param

        header = list(filter(lambda home: home.property == 'property', self.data_sorted))
        search_for_filter, value_for_filter = search_for_user_param()

        if search_for_filter == 'property':
            property = list(filter(lambda home: home.property == value_for_filter, self.data_sorted))
            self.loop_for_table_in_terminal(header)
            self.loop_for_table_in_terminal(property)

        elif search_for_filter == 'building_id':
            building = list(filter(lambda home: home.building_id == value_for_filter, self.data_sorted))
            self.loop_for_table_in_terminal(header)
            self.loop_for_table_in_terminal(building)

        elif search_for_filter == 'owner_acquisition_date':
            owner_acquisition = list(
                filter(lambda home: home.owner_acquisition_date == value_for_filter, self.data_sorted))
            self.loop_for_table_in_terminal(header)
            self.loop_for_table_in_terminal(owner_acquisition)

        elif search_for_filter == 'street1':
            street = list(filter(lambda home: home.street1 == value_for_filter, self.data_sorted))
            self.loop_for_table_in_terminal(header)
            self.loop_for_table_in_terminal(street)

        elif search_for_filter == 'city':
            city = list(filter(lambda home: home.city == value_for_filter, self.data_sorted))
            self.loop_for_table_in_terminal(header)
            self.loop_for_table_in_terminal(city)

        elif search_for_filter == 'zip':
            zip = list(filter(lambda home: home.zip == value_for_filter, self.data_sorted))
            self.loop_for_table_in_terminal(header)
            self.loop_for_table_in_terminal(zip)

        elif search_for_filter == 'lastname':
            lastname = list(filter(lambda home: home.lastname == value_for_filter, self.data_sorted))
            self.loop_for_table_in_terminal(header)
            self.loop_for_table_in_terminal(lastname)

        elif search_for_filter == 'firstname':
            firstname = list(filter(lambda home: home.firstname == value_for_filter, self.data_sorted))
            self.loop_for_table_in_terminal(header)
            self.loop_for_table_in_terminal(firstname)

        elif search_for_filter == 'email':
            email = list(filter(lambda home: home.email == value_for_filter, self.data_sorted))
            self.loop_for_table_in_terminal(header)
            self.loop_for_table_in_terminal(email)

        else:
            print("The word's section match with anything !!! retry please")

        return self.input_choice_first_menu_from_view()


def main_c():
    c = Control()
    c.input_choice_first_menu_from_view()


if __name__ == "__main__":
    main_serializer()
    main_c()
