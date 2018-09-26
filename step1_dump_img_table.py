#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     26-09-2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# StdLib
import logging
import argparse
import os
import csv
# Remote libraries
import sqlite3
# local
from common import *# Things like logging setup











def dump_table_range(database, table_name, start_position, stop_position, output_filepath):
    """
    database should be a sqlAlchemy database object
    table_name should be a valid table name in database
    start_position and stop_position are inclusive.
    output_filepath will be where a .csv file will go
    """
    logging.debug('dump_table() locals() = {0!r}'.format(locals()))# Record arguments

    # Perform search operation

    # Save rows to CSV file

    return



def cli():
    """Command line running"""
    # Handle command line args
    parser = argparse.ArgumentParser()
##    parser.add_argument('booru_url_template', help='booru_url_template',
##                    type=str)
##    parser.add_argument('output_path', help='output_path',
##                    type=str)
    parser.add_argument('low', help='low id (inclusive)',
                    type=int)
    parser.add_argument('high', help='high id (exclusive)',
                    type=int)
    args = parser.parse_args()

    logging.debug('args: {0!r}'.format(args))# Record CLI arguments

    logging.info('exiting cli()')
    return


def dev():
    """For development/debugging in IDE/editor without CLI arguments"""
    logging.warning('running dev()')

    # Dump a table
    dump_table(
        database,
        table_name='',
        start_position=0,
        output_filepath=os.path.join('debug', 'step1_dump_img_table', 'img.csv')
    )

    logging.warning('exiting dev()')
    return


def main():
    dev()
    return


if __name__ == '__main__':
    setup_logging(os.path.join("debug", "step1_dump_img_table.log.txt"))# Setup logging
    try:
        main()
    # Log exceptions
    except Exception, e:
        logging.critical("Unhandled exception!")
        logging.exception(e)
    logging.info( "Program finished.")
