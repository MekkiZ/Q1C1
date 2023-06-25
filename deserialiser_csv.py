"""system module."""

import shutil
import glob
import csv
import os

# the path of the csv files to combine
path = os.path.abspath('DATAS/data/')
allFiles = glob.glob(path + "/*.csv")
in_file_path = os.path.abspath('DATAS/in_file.csv')


def create_new_csv():
    """
    create and link all csv in data files.

    """
    try:
        with open('DATAS/new.csv', 'wb', ) as outfile:
            for i, files_name in enumerate(allFiles):
                print(i, files_name)
                with open(files_name, 'rb') as infile:
                    if i != 0:
                        infile.readline()
                        # away header on all but first file
                    # Block copy rest of file from input to output without parsing
                    shutil.copyfileobj(infile, outfile)
    except ValueError:
        print("Problem From file's folder, please check")


def creat_csv_cleaning():
    """
    Clean data in csv and create new csv cleaned.
    This function has purpose for clean csv, we can choice do not.

    """
    with open('DATAS/new.csv', newline='') as in_file:
        with open('DATAS/in_file.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                # we check all blanck row and delete it
                if any(field.strip() for field in row):
                    writer.writerow(row)
            os.remove(os.path.abspath('DATAS/new.csv'))


def main_serializer():
    """
    This function verify and delete old file merge csv and create the new with the upper function
    with clean also the blank rows

    """
    try:
        create_new_csv()
        if os.path.isfile(os.path.abspath('DATAS/new.csv')):
            # We check if old file is already here
            creat_csv_cleaning()
    except ValueError:
        print("No File in file")


main_serializer()
