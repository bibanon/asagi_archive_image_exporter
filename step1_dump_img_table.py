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
##import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
# local
from common import *# Things like logging setup






def dump_partial_table(connection_string, table_name, csv_filepath, lower_bound=None, upper_bound=None):
    """Export a range from the table to a CSV file"""
    logging.debug('dump_partial_table() locals() = {0!r}'.format(locals()))# Record arguments. WARNING: It is dangerous to record connection string!
    # Ensure output dir exists
    output_dir = os.path.dirname(csv_filepath)
    if not os.path.exists(output_dir):
        logging.debug('Creating output_dir = {0!r}'.format(output_dir))
        os.makedirs(output_dir)
        assert(os.path.exists(output_dir))# Make damn sure we have somewhere to put files before we put any load on the DB.

    # https://stackoverflow.com/questions/2952366/dump-csv-from-sqlalchemy

    Base = automap_base()
    engine = create_engine(connection_string, echo=True)# https://docs.sqlalchemy.org/en/latest/core/engines.html#sqlite
    Base.prepare(engine, reflect=True)

    # Map the tables
    Images = Base.classes[table_name]
    session = Session(engine, autoflush=False)

    if (lower_bound and upper_bound):
        # Select the subset between the supplied values.
        logging.info('Selecting media in range: {0!r} to {1!r}'.format(lower_bound, upper_bound))
        range_images_q = session.query(Images)\
            .filter(Images.media >= lower_bound)\
            .filter(Images.media <= upper_bound)
    elif (upper_bound):
        # Select the subset below or equal to upper_bound.
        logging.info('Selecting media below {0!r}'.format(upper_bound))
        range_images_q = session.query(Images)\
            .filter(Images.media <= upper_bound)
    elif (lower_bound):
        # Select the range above or equal to the lower_bound.
        logging.info('Selecting media above {0!r}'.format(lower_bound))
        range_images_q = session.query(Images)\
            .filter(Images.media >= lower_bound)
    else:
        # Select everything.
        logging.info('Selecting all media')
        range_images_q = session.query(Images)

    logging.info('len(range_images_q.all()) = {0}'.format(len(range_images_q.all())))# PERFORMANCE This might cause slowdowns, disable outside testing

    with open(csv_filepath, 'wb') as csvfile:
        outcsv = csv.writer(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_ALL, lineterminator='\n')

        # Write header
        header = Images.__table__.columns.keys()
        outcsv.writerow(header)

        # Write records
        for record in range_images_q.all():# Write only images in the specified range
            outrow = [getattr(record, c) for c in header ]
##            print('outrow = {0!r}'.format(outrow))# PERFORMANCE This might cause slowdowns, disable outside testing
            outcsv.writerow(outrow)

    assert(os.path.exists(csv_filepath))# Be sure an output file was created.
    logging.info('Finished dumping table {0} to {1}'.format(table_name, csv_filepath))
    return


def dump_table(connection_string, table_name, csv_filepath):
    logging.debug('dump_table() args = {0!r}'.format(locals()))# Record arguments !DANGEROUS TO LOG CREDENTIALS!
    # https://stackoverflow.com/questions/2952366/dump-csv-from-sqlalchemy
    return dump_partial_table(
        connection_string,
        table_name,
        csv_filepath,
        lower_bound=None,
        upper_bound=None
    )


def dev():
    """For development/debugging in IDE/editor without CLI arguments"""
    logging.warning('running dev()')
    import config

    # Dump a table
    dump_table(
        connection_string=config.CONNECT_STRING,
        table_name=config.TABLE_NAME,
        csv_filepath=config.CSV_FILEPATH
    )

##    # Dump a range within a table
##    dump_partial_table(
##        connection_string=config.CONNECT_STRING,
##        table_name=config.TABLE_NAME,
##        csv_filepath=config.CSV_FILEPATH,
##        lower_bound='1536638719722.webm',
##        stop_at=None
##    )

    logging.warning('exiting dev()')
    return


def cli():
    """Command line running"""
    # Handle command line args
    parser = argparse.ArgumentParser()
    parser.add_argument('connection_string', help='connection_string see https://docs.sqlalchemy.org/en/latest/core/engines.html',# https://docs.sqlalchemy.org/en/latest/core/engines.html
                    type=str)
    parser.add_argument('table_name', help='table_name',
                    type=str)
    parser.add_argument('csv_filepath', help='csv_filepath',
                    type=str)
    parser.add_argument('lower_bound', help='lower_bound',
                    type=str)
    args = parser.parse_args()

    logging.debug('args: {0!r}'.format(args))# Record CLI arguments !DANGEROUS TO LOG CREDENTIALS!

    dump_partial_table(
        connection_string=args.connection_string,
        table_name=args.table_name,
        csv_filepath=args.csv_filepath,
        lower_bound=args.lower_bound,
        upper_bound=None
    )

    logging.info('exiting cli()')
    return


def main():
##    dev()
    cli()
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
