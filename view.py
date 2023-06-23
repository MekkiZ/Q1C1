"""system module."""

import sys


def main_interface():
    """
    Create main interface for user with input function.

    The user can search and display all homes.

    :return: multiple variable for controllers part.
            1 : option for see all homes.
            2 : option to search specify data.

    """
    print("=========================")
    print("Sélectionner votre choix: ")
    print("1. Afficher les immeubles")
    print("2. Rechercher")
    print("Q. Pour quitter")
    print("=========================")
    choix_option = input("S'il vous plait faite un choix >>  ")
    return choix_option


def prt_width(item_string: str, width: int):
    """
    This function parameters the table with this data and size.
    :param item_string: data from csv in str
    :param width: and width calculate for create good table

    """
    sys.stdout.write('|' + item_string + ' ' * (width - len(item_string)) + '|')
    sys.stdout.flush()


def search_for_user_param():
    """
    This function create and verify what user choice.
    :return:
    """
    list_input = ['property', 'building_id', 'owner_acquisition_date', 'street1', 'city', 'zip', 'lastname',
                  'firstname', 'email']
    print("=========================")
    print("Sélectionner votre choix parmis ces options: ")
    print("-> property (ex: 0046) "
          "  ->building_id (ex: 1027)"
          "  -> owner_acquisition_date (ex: 2022-08-03)"
          "  -> street1 (ex: 445 RUE PIERRE CAMPION)"
          "  -> city (ex: ALENCON)"
          "  -> zip (ex: 93250)"
          "  -> lastname (ex: COTTI)"
          "  -> firstname (ex: ETIENN)"
          "  -> email (ex: 487886@gmail.com)")
    print("=========================")
    search_choice = input("S'il vous plait faite un choix (ex: email ) :  >>  ")
    search_value = input("S'il vous plait renseignez une valeur (ex : toto@gmail.com ) :  >>  ")
    if search_choice in list_input:
        return search_choice, search_value
    else:
        return search_for_user_param()



