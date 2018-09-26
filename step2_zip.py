#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     27-09-2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# StdLib
import logging
import argparse
import os
import csv
import zipfile
# Remote libraries
# local
from common import *# Things like logging setup




def dev():
    """For development/debugging in IDE/editor without CLI arguments"""
    logging.warning('running dev()')


    logging.warning('exiting dev()')
    return


def main():
##    dev()
    return

def add_to_zip(zip_obj, filepath):
    try:
        zip_obj.write(filepath)
    except WindowsError, err:
        logging.error(err)

if __name__ == '__main__':
    setup_logging(os.path.join("debug", "db_test.log.txt"))# Setup logging
    try:
        main()
    # Log exceptions
    except Exception, e:
        logging.critical("Unhandled exception!")
        logging.exception(e)
    logging.info("Program finished.")




csv_path = os.path.join('data', 'g_images.csv')
zip_path = os.path.join('data', 'g_images.zip')
with zipfile.ZipFile(zip_path, 'w') as myzip:
    with open(csv_path, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            # Add media to zip
            if row['media']:
##                myzip.write(row['media'])
                add_to_zip(zip_obj=myzip, filepath=row['media'])
            # Add preview_op to zip
            if row['preview_op']:
##                myzip.write(row['preview_op'])
                add_to_zip(zip_obj=myzip, filepath=row['preview_op'])
            # Add preview_reply to zip
            if row['preview_reply']:
##                myzip.write(row['preview_reply'])
                add_to_zip(zip_obj=myzip, filepath=row['preview_reply'])


