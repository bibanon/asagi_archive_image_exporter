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
import config





def add_to_zip(zip_obj, filepath):
    try:
        zip_obj.write(filepath)
    except WindowsError, err:
        logging.error(err)
    return


def zip_from_csv(csv_path, zip_path):
    logging.info('Zipping files in {0} to {1}'.format(csv_path, zip_path))
    row_counter = 0
    with zipfile.ZipFile(zip_path, 'w') as myzip:
        with open(csv_path, 'rb', ) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)
            for row in reader:
                row_counter += 1
                if (row_counter % 100 == 0):
                    logging.info('Processed {0} rows.'.format(row_counter))
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
    logging.info('Finished zipping files from {0} rows in {1} to {2}'.format(row_counter, csv_path, zip_path))
    return


def cli():
    """Command line running"""
    # Handle command line args
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path', help='csv_path',
                    type=str)
    parser.add_argument('zip_path', help='zip_path',
                    type=str)
    args = parser.parse_args()

    logging.debug('args: {0!r}'.format(args))# Record CLI arguments

    zip_from_csv(csv_path=args.csv_path, zip_path=args.zip_path)

    logging.info('exiting cli()')
    return


def dev():
    """For development/debugging in IDE/editor without CLI arguments"""
    logging.warning('running dev()')

    csv_path = config.CSV_FILEPATH
    zip_path = config.ZIP_PATH
    zip_from_csv(csv_path, zip_path)

    logging.warning('exiting dev()')
    return


def main():
    dev()
    return

if __name__ == '__main__':
    setup_logging(os.path.join("debug", "step2_zip.log.txt"))# Setup logging
    try:
        main()
    # Log exceptions
    except Exception, e:
        logging.critical("Unhandled exception!")
        logging.exception(e)
    logging.info("Program finished.")







